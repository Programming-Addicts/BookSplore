import asyncpg


async def StartConnection():
    return await asyncpg.connect("postgresql://postgres@localhost/booksplore?password=123")

async def CloseConnection(db: asyncpg.connection.Connection):
    await db.close()

async def CreateTables(db: asyncpg.connection.Connection):
    await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT UNIQUE,
            email TEXT UNIQUE,
            hashed_password TEXT,
            PRIMARY KEY (username, email)
        );
    """)
