from    database.utils.user import get_user
from database.database import Database
from models.reviews import Review
import json

async def get_reviews(db:Database, book_id = None, user_id = None, offset = 0):
    query = """SELECT * FROM reviews WHERE """
    if book_id is not None:
        query += "book_id = $1 "
    elif user_id is not None:
        query += "user_id = $1 "
    else:
        return None
    query += "ORDER BY timestamp OFFSET $2 LIMIT 10"
    records = await db.fetch(query, book_id or user_id, offset)
    reviews = []
    for record in records:
        review = Review(**record)
        user_id = review.user_id
        user = await get_user(db , id=user_id)
        book = await db.fetchrow("SELECT title, image_links FROM cached_books WHERE book_id = $1", review.book_id)
        if book is None:
            continue
        user_data = dict(user)
        review_data = dict(review)
        del review_data['user_id']
        del user_data['email']
        if review.stay_anonymous:
            user_data['first_name'] = 'Anonnymous'
            for key in ['id', 'last_name', 'discriminator', 'username', 'avatar_url', 'followers', 'following']:
                user_data[key] = None
        review_data['user'] = user_data
        review_data['book_data'] = {'title' : book['title'], 'image_links' : json.loads(book['image_links'])}
        reviews.append(review_data)

    return reviews


async def create_review(db:Database, review: Review):
    query = """INSERT INTO reviews (book_id, user_id, stay_anonymous, content, rating) VALUES ($1, $2, $3, $4, $5)"""
    await db.execute(query, review.book_id, review.user_id, review.stay_anonymous, review.content, review.rating)