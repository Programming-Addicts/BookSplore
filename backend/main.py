from fastapi import FastAPI
import dotenv
import os

from starlette.config import Config
from starlette.middleware.sessions import SessionMiddleware

from endpoints import follow
from database.database import Database

config = Config(".env")

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("SECRET_KEY"))

#app.include_router(home.router)
app.include_router(follow.router)
#app.include_router(auth.router)


@app.on_event("startup")
async def on_startup():
    dotenv.load_dotenv('.env')
    app.state.db = await Database.create_pool(app, uri=os.environ.get("DB_URI"))

@app.on_event("shutdown")
async def shutdown():
    await app.state.db.close_connection()
