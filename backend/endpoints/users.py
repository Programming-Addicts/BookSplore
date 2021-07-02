import json
from typing import Optional
import os
import jwt
import dotenv
from fastapi import APIRouter, Request, Header
from fastapi.responses import JSONResponse
from database.utils.user import get_user
from models.users import User

router = APIRouter(tags=["Users"])

dotenv.load_dotenv('.env')
secret_key = os.environ.get("SECRET_KEY")

@router.get('/get')
async def fetch_user(request: Request, id: int = None, authorization: Optional[str] = Header(None)):
    try:
        user_id = jwt.decode(authorization, secret_key, algorithms="HS256").get("id")
    except:
        return JSONResponse({'Error': 'Incorrect Authorization Token'}, status_code=401)
    if id is not None:
        user_id = id
    user = await get_user(request.app.state.db, id=user_id)
    if user is not None:
        user.followers  = json.loads(user.followers)
        user.following = json.loads(user.following)
        user_data = dict(user)
        review_count = await request.app.state.db.fetchrow("SELECT COUNT(*) FROM reviews WHERE user_id = $1", user.id)
        user_data['total_reviews'] = int(review_count['count'])
        del user_data['recent_books']
        del user_data['email']
        return user_data
    else:
        return JSONResponse({'None': 'No user is authenticated'}, status_code=401)

@router.get('/search')
async def search_user(request: Request, username: str):
    users = []
    records = await request.app.state.db.fetch("SELECT * FROM users WHERE username LIKE $1 LIMIT 10", "%"+username+"%")
    print(records)
    if records:
        for user in records:
            data = {'id': user['id'],
                    'first_name': user['first_name'],
                    'last_name': user['last_name'],
                    'discriminator' : user['discriminator'],
                    'username': user['username'], 
                    'email': user['email'],
                    'avatar_url': user['avatar_url'],
                    'followers' : user['followers'],
                    'following' : user['following']}
            user = User(**data)
            user_data = dict(user)
            review_count = await request.app.state.db.fetchrow("SELECT COUNT(*) FROM reviews WHERE user_id = $1", user.id)
            user_data['total_reviews'] = int(review_count['count'])
            del user_data['email']
            users.append(user_data)
        return users
    else:
        return JSONResponse({'None': 'No such user with the given username found.'}, status_code=404)

@router.get('/recent-books')
async def get_recent_books(request: Request, user_id: int):
    db = request.app.state.db
    user = await get_user(db, id=user_id)
    recent_book_ids = json.loads(user.recent_books)[10::-1]
    recent_books = []
    for id in recent_book_ids:
        book = await db.fetchrow("SELECT * FROM cached_books WHERE id = $1", id)
        if book is None:
            continue
        book_data = {'book_id': book['book_id'],
                     'title': book['title'],
                     'image_links': json.loads(book['image_links'])}
        recent_books.append(book_data)

    return recent_books 
