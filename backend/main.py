from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import os
import dotenv

from starlette.config import Config
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from endpoints import home, follow, auth, users, books
from database.database import Database

config = Config(".env")

app = FastAPI()

app.mount("/dist", StaticFiles(directory="dist/"), name="dist")
app.mount("/css", StaticFiles(directory="dist/css"), name="css")
app.mount("/img", StaticFiles(directory="dist/img"), name="img")
app.mount("/js", StaticFiles(directory="dist/js"), name="js")

templates = Jinja2Templates(directory="dist")

origins = [
    "http://localhost:8000",
    "http://localhost:8080",
    "https://booksplore.milindm.me",
    "https://booksplore.netlify.app"
]

app.add_middleware(SessionMiddleware, secret_key=os.environ.get("SECRET_KEY"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(follow.router)
app.include_router(auth.router)
app.include_router(books.router)
app.include_router(users.router)

@app.on_event("startup")
async def on_startup():
    dotenv.load_dotenv('.env')
    app.state.db = await Database.create_pool(app, uri=os.environ.get("DB_URI"))

@app.on_event("shutdown")
async def shutdown():
    await app.state.db.close_connection()

@app.get("/{full_path:path}")
async def serve_frontend(request: Request, full_path: str):
    if full_path == "favicon.ico":
        return FileResponse("dist/favicon.ico")
    return templates.TemplateResponse("index.html", {"request": request})
