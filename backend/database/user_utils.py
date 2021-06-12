import asyncpg

from . import database
from models.user import User

async def CreateNewUser(db: asyncpg.connection.Connection, user: User):

    result = await db.fetchval(
        """
        INSERT INTO users
            (username, email, hashed_password)
            VALUES ($1, $2, $3)
        ON CONFLICT("username", "email") DO NOTHING
        RETURNING 'No Conflict';
        """,
        user.name, user.email, user.hashed_password,
    )

    return result is None
