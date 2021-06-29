from typing import Optional

import os

from fastapi import APIRouter, Request, Header
import jwt
import dotenv

from starlette.config import Config
from fastapi.responses import RedirectResponse, JSONResponse
from authlib.integrations.starlette_client import OAuth

from database.utils.user import get_user, update_user, create_user
from models.users import User

router = APIRouter(tags=["Google Authentication"])

dotenv.load_dotenv('.env')
config = Config('.env')
oauth = OAuth(config)
CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
oauth.register(
    name='google',
    server_metadata_url=CONF_URL,
    client_kwargs={
        'scope': 'openid email profile'
    }
)

secret_key = os.environ.get("SECRET_KEY")

@router.get('/login')
async def login(request: Request):
    # Redirect Google OAuth back to our application
    redirect_uri = request.url_for('auth')
    return await oauth.google.authorize_redirect(request, redirect_uri)


@router.route('/auth')
async def auth(request: Request):
    # Perform Google OAuth
    token = await oauth.google.authorize_access_token(request)
    req_user = await oauth.google.parse_id_token(request, token)
    db = request.app.state.db
    user = await get_user(db, email=req_user['email'])
    if user is None:
        user = User(**{'email': req_user['email']})
        await create_user(db, user)

    # Updates name and profile picture in the database if changed
    user.first_name = req_user['given_name']
    user.last_name = req_user['family_name']
    user.avatar_url = req_user['picture']

    token = jwt.encode(
        {"id": user.id},
        key=secret_key,
        algorithm="HS256"
    )

    user.token = token

    await update_user(db, user)
    resp =  RedirectResponse(f"/dev/dashboard")
    resp.headers['Authorization'] = token
    return resp


@router.get('/logout')
async def logout(request: Request, authorization: Optional[str] = Header(None)):
    try:
        user_id = jwt.decode(authorization, secret_key, algorithms="HS256").get('id')
    except:
        return JSONResponse({'Error': 'Incorrect Authorization Token'}, status_code=401)
    user = await get_user(request.app.state.db, id=user_id)
    user.token = None
    update_user(request.app.state.db, user)
    return RedirectResponse(url='/')
