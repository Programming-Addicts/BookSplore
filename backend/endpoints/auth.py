from typing import Optional

import os
import random

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
    try:
        return await oauth.google.authorize_redirect(request, redirect_uri)
    except:
        return {'Error' : 'Some error occurred during the authentication'}


@router.route('/auth')
async def auth(request: Request):
    # Perform Google OAuth
    token = await oauth.google.authorize_access_token(request)
    req_user = await oauth.google.parse_id_token(request, token)
    db = request.app.state.db
    user = await get_user(db, email=req_user['email'])
    first_name = req_user['given_name']
    last_name = req_user['family_name']
    if user is None:
        user = User(**{'first_name': first_name,
                       'last_name': last_name,
                       'email': req_user['email']})
        discrims_for_given_name = await db.fetch("SELECT discriminator FROM users WHERE first_name = $1 AND last_name = $2", req_user['given_name'], req_user['family_name'])
        discrims_for_given_name = [record['discriminator'] for record in discrims_for_given_name]
        if len(discrims_for_given_name) >= 8999:
            last_name += str(random.randint(1,100))

        discriminator = random.randint(1000,9999)
        while discriminator in discrims_for_given_name:
            discriminator = random.randint(1000,9999)

        user.discriminator = discriminator
        user.username = user.first_name.replace(' ', '') + user.last_name.replace(' ', '') + '#' + str(user.discriminator)
        user = await create_user(db, user)
        

    # Updates name and profile picture in the database if changed
    user.avatar_url = req_user['picture']
    await update_user(db, user)

    token = jwt.encode(
        {"id": user.id},
        key=secret_key,
        algorithm="HS256"
    )
    return RedirectResponse(f"/dashboard?token={token}")


@router.get('/logout')
async def logout():
    return RedirectResponse(url='/')
