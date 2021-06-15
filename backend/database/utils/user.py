from database.database import Database
from models.users import User

async def get_user(db:Database, email):
    user = await db.fetchrow("SELECT * FROM users WHERE email = $1", email)
    if user is None:
        return None
    data = {'first_name': user['first_name'],
            'last_name': user['last_name'],
            'email': user['email'],
            'avatar_url': user['avatar_url']}
    return User(**data)
async def create_user(db:Database, user: User):
    query = """INSERT INTO users (first_name, last_name, email, avatar_url) VALUES ($1, $2, $3, $4)"""
    await db.execute(query, user.first_name, user.last_name, user.email, user.avatar_url)

async def update_user(db:Database, user:User):
    query = """UPDATE users SET first_name = $1, last_name = $2, avatar_url = $3 WHERE email = $4"""
    await db.execute(query, user.first_name, user.last_name, user.avatar_url, user.email)
