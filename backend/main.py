from fastapi import FastAPI
import dotenv
import os

from starlette.config import Config
from starlette.middleware.sessions import SessionMiddleware
from fastapi.middleware.cors import CORSMiddleware

from endpoints import follow, auth, home, books
from database.database import Database

config = Config(".env")

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost:8080",
]

app.add_middleware(SessionMiddleware, secret_key=os.environ.get("SECRET_KEY"))

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(home.router)
app.include_router(follow.router)
app.include_router(auth.router)
app.include_router(books.router)

@app.on_event("startup")
async def on_startup():
    dotenv.load_dotenv('.env')
    app.state.db = await Database.create_pool(app, uri=os.environ.get("DB_URI"))

@app.on_event("shutdown")
async def shutdown():
    await app.state.db.close_connection()
