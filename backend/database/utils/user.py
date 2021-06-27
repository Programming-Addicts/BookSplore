from database.database import Database
from models.users import User
import json

async def get_user(db:Database, id = None, email=None):
    if email and id:
        return {"Bad Request" : "Search with id or email"}
    query = "SELECT * FROM users WHERE "
    if email is not None:
        query += "email = $1"
    else:
        query += "id = $1"
    user = await db.fetchrow(query, id if email is None else email)
    if user is None:
        return None
    data = {'id': user['id'],
            'first_name': user['first_name'],
            'last_name': user['last_name'],
            'email': user['email'],
            'avatar_url': user['avatar_url'],
            'followers' : user['followers'],
            'following' : user['following']}
    return User(**data)


async def create_user(db:Database, user: User):
    query = """INSERT INTO users (first_name, last_name, email, avatar_url) VALUES ($1, $2, $3, $4)"""
    await db.execute(query, user.first_name, user.last_name, user.email, user.avatar_url)
    return await get_user(db, email=user.email)


async def update_user(db:Database, user:User):
    query = """UPDATE users SET first_name = $1, last_name = $2, avatar_url = $3 WHERE email = $4"""
    await db.execute(query, user.first_name, user.last_name, user.avatar_url, user.email)

async def get_followers_and_following(db:Database, user: User):
    query = """SELECT followers, following FROM users WHERE id = $1"""
    record = await db.fetchrow(query, user.id)
    data = {'followers' : json.loads(record['followers']), 'following' : json.loads(record['following'])}
    return data