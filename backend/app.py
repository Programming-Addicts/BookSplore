from fastapi import FastAPI

from endpoints import user_endpoint, follow_endpoint
from database import database

app = FastAPI()

app.include_router(user_endpoint.router)
app.include_router(follow_endpoint.router)

@app.on_event("startup")
async def on_startup():
    app.state.db = await database.StartConnection()
    await database.CreateTables(app.state.db)

@app.on_event("shutdown")
async def shutdown():
    await database.CloseConnection(app.state.db)
