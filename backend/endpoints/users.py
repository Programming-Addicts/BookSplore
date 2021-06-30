from typing import Optional
import os
import jwt
import dotenv
from fastapi import APIRouter, Request, Header
from fastapi.responses import JSONResponse
from database.utils.user import get_user

router = APIRouter(tags=["Users"])

dotenv.load_dotenv('.env')
secret_key = os.environ.get("SECRET_KEY")

@router.get('/current')
async def get_current_user(request: Request, authorization: Optional[str] = Header(None)):
    try:
        user_id = jwt.decode(authorization, secret_key, algorithms="HS256").get("id")
    except:
        return JSONResponse({'Error': 'Incorrect Authorization Token'}, status_code=401)
    user = await get_user(request.app.state.db, id=user_id)
    if user is not None:
        user_data = dict(user)
        del user_data['email']
        return user_data
    else:
        return JSONResponse({'None': 'No user is authenticated'}, status_code=401)

@router.get('/search')
async def search_user(request: Request, username: str):
    user = await get_user(request.app.state.db, username=username)
    if user is not None:
        user_data = dict(user)
        del user_data['email']
        return user_data
    else:
        return JSONResponse({'None': 'No such user with the given username found.'}, status_code=404)
