from fastapi import FastAPI
import dotenv
import os


from endpoints import user_endpoint, follow_endpoint
from database.database import Database

app = FastAPI()

app.include_router(user_endpoint.router)
app.include_router(follow_endpoint.router)

@app.on_event("startup")
async def on_startup():
    dotenv.load_dotenv('.env')
    app.state.db = await Database.create_pool(app, uri=os.environ.get("DB_URI"))

@app.on_event("shutdown")
async def shutdown():
    await app.state.db.close_connection()