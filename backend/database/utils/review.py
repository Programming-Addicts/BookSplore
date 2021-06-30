from database.database import Database
from models.reviews import Review

async def get_reviews(db:Database, book_id = None):
    query = """SELECT * FROM reviews WHERE book_id = $1"""
    records = await db.fetch(query, book_id)
    reviews = []
    for record in records:
        review = Review(**record)
        reviews.append(review)

    return reviews


async def create_review(db:Database, review: Review):
    query = """INSERT INTO reviews (book_id, user_id, stay_anonymous, content, rating) VALUES ($1, $2, $3, $4, $5)"""
    await db.execute(query, review.book_id, review.user_id, review.stay_anonymous, review.content, review.rating)