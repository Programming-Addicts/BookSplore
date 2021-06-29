from typing import Optional
import os
import jwt
import dotenv
from fastapi import APIRouter, Request, Header
from fastapi.responses import JSONResponse
from models.users import User
from database.utils.user import get_user

router = APIRouter(tags=["Users"])

dotenv.load_dotenv('.env')
secret_key = os.environ.get("SECRET_KEY")

@router.get('/current')
async def get_current_user(request: Request, authorization: Optional[str] = Header(None)):
    try:
        user_id = jwt.decode(authorization, secret_key, algorithms="HS256").get("id")
    except:
        return JSONResponse({'None': 'No user is authenticated'}, status_code=401)
    user = await get_user(request.app.state.db, id=user_id)
    if user is not None:
        return user
    else:
        return JSONResponse({'None': 'No user is authenticated'}, status_code=401)
