from datetime import datetime
from models.reviews import Review
from typing import Optional
from fastapi import APIRouter, Request, Header, Form
from fastapi.responses import JSONResponse
import os
import jwt
from aiohttp import request as aiorequest
import dotenv
from database.utils.user import get_user
from database.utils.review import create_review, get_reviews
from .utils.language import get_language

dotenv.load_dotenv('.env')
api_key = os.environ.get('GOOGLE_API_KEY')
secret_key = os.environ.get("SECRET_KEY")
router = APIRouter(tags=["Books"])


@router.get('/search')
async def search(request: Request, query: str = None, book_id: str = None, limit: int = 20, offset: int = 0, download: bool = False,
                 filter: str = None, sorting: str = "relevance"):
    if not (query or book_id or limit > 40):
        return JSONResponse({'Error': 'Please enter valid search parameters'}, status_code=400)
    url = 'https://www.googleapis.com/books/v1/volumes'
    params = {'key': api_key, 'q': query, 'maxResults': limit, 'startIndex' : offset}

    if filter in ['partial', 'full', 'free-ebooks', 'paid-ebooks', 'ebooks']:
        params['filter'] = filter

    if download:
        params['download'] = 'epub'

    if sorting in ['relevance', 'newest']:
        params['orderBy'] = sorting

    if book_id is not None:
        url = f"https://www.googleapis.com/books/v1/volumes/{book_id}"
        del params
        params = {'key': api_key}

    async with aiorequest('GET', url, params=params) as response:
        data = await response.json()
        books = []
        if data.get('totalItems') == 0:
            return JSONResponse({'Invalid Query': 'No books were found.'}, status_code=404)
        all_data = data.get('items') if data.get('items') is not None else [data]
        for book in all_data:
            book_info = book['volumeInfo']
            access_info = book['accessInfo']
            has_pdf = access_info.get('pdf')
            has_epub = access_info.get('epub')
            if download and not (has_epub['isAvailable'] == True) or (has_pdf['isAvailable'] == True) and len(
                    has_epub.keys()) < 2 and len(has_pdf.keys()) < 2:
                continue
            book_data = {'id': book.get('id'),
                         'title': book_info.get('title'),
                         'authors': book_info.get('authors'),
                         'description': book_info.get('description'),
                         'publisher': book_info.get('publisher'),
                         'publish_date': book_info.get('publishedDate'),
                         'language': get_language(book_info.get('language')),
                         'avg_rating': book_info.get('averageRating'),
                         'total_ratings': book_info.get('ratingsCount'),
                         'isbns': book_info.get('industryIdentifiers'),
                         'page_count': book_info.get('pageCount'),
                         'image_links': book_info.get('imageLinks'),
                         'preview_link': book_info.get('previewLink'),
                         'pdf': has_pdf,
                         'epub': has_epub
                         }
            books.append(book_data)

        return books if book_id is None else books[0]

@router.post('/review')
async def post_review(request: Request, authorization: Optional[str] = Header(None),
                      book_id: str = Form(...),
                      stay_anonymous: bool = Form(...),
                      content: str = Form(...),
                      rating: int = Form(...)):
    try:
        user_id = jwt.decode(authorization, secret_key, algorithms="HS256").get("id")
    except:
        return JSONResponse({'Error': 'Incorrect Authorization Token'}, status_code=401)

    # print(book_id, user_id, stay_annonymous, content, rating, sep="\n\n\n\n")

    review = Review(book_id=book_id,
                    user_id=user_id,
                    stay_anonymous=stay_anonymous,
                    content=content,
                    rating=rating)

    user = await get_user(request.app.state.db, id=user_id)
    if user is not None:
        try:
            await create_review(request.app.state.db, review=review)
        except:
            return JSONResponse({'Error' : 'Invalid Request Body'} , status_code=400)
        return {'Success' : 'Review successfully posted'}
    else:
        return JSONResponse({'None': 'No user is authenticated'}, status_code=401)

@router.get('/review')
async def get_review(request: Request, book_id: str):
    return await get_reviews(request.app.state.db, book_id=book_id)