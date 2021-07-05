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

from endpoints import follow, auth, users, books
from database.database import Database

config = Config(".env")

app = FastAPI()

# Specifying directories for serving files in development, production uses nginx.
app.mount("/dist", StaticFiles(directory="dist/"), name="dist")
app.mount("/css", StaticFiles(directory="dist/css"), name="css")
app.mount("/img", StaticFiles(directory="dist/img"), name="img")
app.mount("/js", StaticFiles(directory="dist/js"), name="js")

templates = Jinja2Templates(directory="dist")

origins = [
    "https://booksplore.tech"
]

# Sessions middleware for Google Authentication.
app.add_middleware(SessionMiddleware, secret_key=os.environ.get("SECRET_KEY"))

# Setting uprintp CORS middleware.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(follow.router, prefix="/api")
app.include_router(auth.router, prefix="/api")
app.include_router(books.router, prefix="/api/books")
app.include_router(users.router, prefix="/api/users")

# Connecting to the database and setting it as a state variable.
@app.on_event("startup")
async def on_startup():
    dotenv.load_dotenv('.env')
    app.state.db = await Database.create_pool(app, uri=os.environ.get("DB_URI"))
    if os.environ.get('INIT') == 'True':
        with open('tables.sql') as f:
            await app.state.db.execute(f.read())
        print("Initialized the database. You may now turn INIT to false in your .env")

#Closing the database connection when shutting down the app.
@app.on_event("shutdown")
async def shutdown():
    await app.state.db.close_connection()

# Serving index.html from backend from where Vue takes control.
@app.get("/{full_path:path}")
async def serve_frontend(request: Request, full_path: str):
    if full_path == "favicon.ico":
        return FileResponse("dist/favicon.ico")
    return templates.TemplateResponse("index.html", {"request": request})
