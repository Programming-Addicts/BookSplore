import json
from datetime import time, timedelta
from models.reviews import Review
from typing import Optional
from fastapi import APIRouter, Request, Header, Form
from fastapi.responses import JSONResponse
import os
import jwt
from aiohttp import request as aiorequest
import dotenv
from database.utils.user import get_user
from database.utils.review import create_review, get_reviews, get_review
from .utils.language import get_language
from .utils.events import review_event

dotenv.load_dotenv(".env")
api_key = os.environ.get("GOOGLE_API_KEY")
secret_key = os.environ.get("SECRET_KEY")
router = APIRouter(tags=["Books"])


# To search books with custom parametres sent to google api.
@router.get("/search")
async def search(
    request: Request,
    query: str,
    limit: int = 20,
    offset: int = 0,
    download: bool = False,
    filter: str = None,
    sorting: str = "relevance",
    authorization: Optional[str] = Header(None),
):
    try:
        # Ensures that only an authenticated user can make a search.
        _ = jwt.decode(authorization, secret_key, algorithms="HS256").get("id")
    except:
        return JSONResponse({"Error": "Incorrect Authorization Token"}, status_code=401)
    if limit > 40:
        return JSONResponse(
            {"Error": "Please enter valid search parameters"}, status_code=400
        )
    url = "https://www.googleapis.com/books/v1/volumes"

    params = {"key": api_key, "q": query, "maxResults": limit, "startIndex": offset}

    if filter in ["partial", "full", "free-ebooks", "paid-ebooks", "ebooks"]:
        params["filter"] = filter

    if download:
        params["download"] = "epub"

    if sorting in ["relevance", "newest"]:
        params["orderBy"] = sorting

    async with aiorequest("GET", url, params=params) as response:
        data = await response.json()
        books = []

        # Data parsing
        if data.get("totalItems") == 0:
            return JSONResponse(
                {"Invalid Query": "No books were found."}, status_code=404
            )

        all_data = data.get("items") if data.get("items") is not None else [data]

        for book in all_data:
            book_info = book.get("volumeInfo")
            if book_info is None:
                return JSONResponse(
                    {"Invalid Query": "No books were found."}, status_code=404
                )
            access_info = book["accessInfo"]
            has_pdf = access_info.get("pdf")
            has_epub = access_info.get("epub")

            if (
                download
                and not (has_epub["isAvailable"] == True)
                or (has_pdf["isAvailable"] == True)
                and len(has_epub.keys()) < 2
                and len(has_pdf.keys()) < 2
            ):
                continue

            id = book.get("id")
            title = book_info.get("title")
            image_links = book_info.get("imageLinks")
            authors = book_info.get("authors")
            description = book_info.get("description")
            book_data = {
                "id": id,
                "title": title,
                "authors": authors,
                "description": description,
                "image_links": image_links,
            }

            books.append(book_data)
            extras = {
                "publisher": book_info.get("publisher"),
                "categories": book_info.get("categories"),
                "publish_date": book_info.get("publishedDate"),
                "language": get_language(book_info.get("language")),
                "avg_rating": book_info.get("averageRating"),
                "total_ratings": book_info.get("ratingsCount"),
                "isbns": book_info.get("industryIdentifiers"),
                "page_count": book_info.get("pageCount"),
                "preview_link": book_info.get("previewLink"),
                "pdf": has_pdf,
                "epub": has_epub,
            }

            save_data = book_data.copy()
            save_data.update(extras)
            await request.app.state.db.execute(
                "INSERT INTO cached_searches (book_id, response) VALUES ($1, $2) ON CONFLICT DO NOTHING",
                id,
                json.dumps(save_data),
            )

        return books


@router.get("/get")
async def get_books_data(
    request: Request, book_id: str, authorization: Optional[str] = Header(None)
):
    try:
        user_id = jwt.decode(authorization, secret_key, algorithms="HS256").get("id")
    except:
        return JSONResponse({"Error": "Incorrect Authorization Token"}, status_code=401)

    db = request.app.state.db
    user = await get_user(db, id=user_id)

    if user is None:
        return JSONResponse({"Error": "Incorrect Authorization Token"}, status_code=401)
    book_data = await db.fetchrow(
        "SELECT response FROM cached_searches WHERE book_id = $1", book_id
    )

    if book_data:
        book_info = json.loads(book_data["response"])

        cache_query = """INSERT INTO cached_books (book_id, title, image_links, categories) VALUES ($1, $2, $3, $4) ON CONFLICT DO NOTHING"""
        await db.execute(
            cache_query,
            book_info["id"],
            book_info.get("title"),
            json.dumps(book_info.get("image_links")),
            json.dumps(book_info.get("categories", "")),
        )

        cache = await db.fetchrow(
            "SELECT id FROM cached_books WHERE book_id = $1", book_info["id"]
        )
        recent_books = json.loads(user.recent_books)
        cached_id = cache.get("id")
        if cached_id in recent_books:
            recent_books.remove(cached_id)
        recent_books = [cache["id"]] + recent_books
        user.recent_books = json.dumps(recent_books[:30])
        await db.execute(
            "UPDATE users SET recent_books = $1 WHERE id = $2",
            user.recent_books,
            user.id,
        )
        return book_info
    else:
        url = f"https://www.googleapis.com/books/v1/volumes/{book_id}"
        params = {"key": api_key}

        async with aiorequest("GET", url, params=params) as response:
            book = await response.json()

            if book.get("totalItems") == 0:
                return JSONResponse(
                    {"Invalid Query ": "No books were found."}, status_code=404
                )

            book_info = book.get("volumeInfo")

            if book_info is None:
                return JSONResponse(
                    {"Invalid Query": "No books were found."}, status_code=404
                )

            access_info = book["accessInfo"]
            has_pdf = access_info.get("pdf")
            has_epub = access_info.get("epub")
            id = book.get("id")
            title = book_info.get("title")
            image_links = book_info.get("imageLinks")
            authors = book_info.get("authors")
            description = book_info.get("description")

            categories = book_info.get("categories")
            cache_query = """INSERT INTO cached_books (book_id, title, image_links, categories) VALUES ($1, $2, $3, $4) ON CONFLICT DO NOTHING"""

            await db.execute(
                cache_query, id, title, json.dumps(image_links), json.dumps(categories)
            )
            cache = await db.fetchrow(
                "SELECT id FROM cached_books WHERE book_id = $1", id
            )
            recent_books = json.loads(user.recent_books)
            cached_id = cache.get("id")
            if cached_id in recent_books:
                recent_books.remove(cached_id)
            recent_books = [cache["id"]] + recent_books
            user.recent_books = json.dumps(recent_books[:30])

            await db.execute(
                "UPDATE users SET recent_books = $1 WHERE id = $2",
                user.recent_books,
                user.id,
            )

            book_data = {
                "id": id,
                "title": title,
                "authors": authors,
                "description": description,
                "categories": categories,
                "publisher": book_info.get("publisher"),
                "publish_date": book_info.get("publishedDate"),
                "language": get_language(book_info.get("language")),
                "avg_rating": book_info.get("averageRating"),
                "total_ratings": book_info.get("ratingsCount"),
                "isbns": book_info.get("industryIdentifiers"),
                "page_count": book_info.get("pageCount"),
                "image_links": image_links,
                "preview_link": book_info.get("previewLink"),
                "pdf": has_pdf,
                "epub": has_epub,
            }

            await request.app.state.db.execute(
                "INSERT INTO cached_searches (book_id, response) VALUES ($1, $2) ON CONFLICT DO NOTHING",
                id,
                json.dumps(book_data),
            )
            return book_data


# Endpoint to post review.
@router.post("/review")
async def post_review(
    request: Request,
    authorization: Optional[str] = Header(None),
    book_id: str = Form(...),
    stay_anonymous: bool = Form(...),
    content: str = Form(...),
    rating: int = Form(...),
):
    db = request.app.state.db
    try:
        user_id = jwt.decode(authorization, secret_key, algorithms="HS256").get("id")
    except:
        return JSONResponse({"Error": "Incorrect Authorization Token"}, status_code=401)

    last_review = await db.fetchrow(
        "SELECT NOW() - timestamp AS last_review FROM reviews WHERE user_id = $1 ORDER BY timestamp DESC LIMIT 1",
        user_id,
    )
    if last_review is not None and last_review.get("last_review") < timedelta(
        minutes=1
    ):
        return JSONResponse(
            {
                "Error": "To prevent spamming, book reviews are rate limited. To post a review again, try again in sometime."
            },
            status_code=400,
        )

    review = Review(
        book_id=book_id,
        user_id=user_id,
        stay_anonymous=stay_anonymous,
        content=content,
        rating=rating,
    )

    user = await get_user(db, id=user_id)

    if user is not None:
        try:
            review = await create_review(db, review=review)
        except:
            return JSONResponse({"Error": "Invalid Request Body"}, status_code=400)
        if not review.stay_anonymous:
            await review_event(db, performer=user.id, target=review.id)

        return {"Success": "Review successfully posted"}
    else:
        return JSONResponse({"None": "No user is authenticated"}, status_code=401)


@router.delete("/review")
async def delete_review(
    request: Request, review_id: int, authorization: Optional[str] = Header(None)
):
    db = request.app.state.db
    try:
        user_id = jwt.decode(authorization, secret_key, algorithms="HS256").get("id")
    except:
        return JSONResponse({"Error": "Incorrect Authorization Token"}, status_code=401)

    review = await get_review(db, id=review_id)
    if user_id in [1, 2, 3, 4] or user_id == review.user_id:
        await db.execute("DELETE FROM reviews WHERE id = $1", review_id)
        return JSONResponse({"Success": "Deleted the book review."}, status_code=200)

    else:
        return JSONResponse(
            {"Error": "You are not authorized to delete this review."}, status_code=401
        )


# Endpoint to get all reviews for a book or user.
@router.get("/reviews")
async def search_reviews(
    request: Request, book_id: str = None, user_id: int = None, offset: int = 0
):
    if book_id and user_id:
        return JSONResponse(
            {"Invalid Query": "Search either by book id OR user id"}, status_code=400
        )

    reviews = []

    if book_id is not None:
        reviews = await get_reviews(
            request.app.state.db, book_id=book_id, offset=offset
        )

    elif user_id is not None:
        reviews = await get_reviews(
            request.app.state.db, user_id=user_id, offset=offset
        )

    return reviews
