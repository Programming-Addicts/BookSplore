import json
from typing import Optional
import jwt
import os
import dotenv

from fastapi import APIRouter, Request, Header
from fastapi.responses import JSONResponse


from database.utils import user as db_user

router = APIRouter(tags=["Follow Users"])
dotenv.load_dotenv('.env')

secret_key = os.environ.get("SECRET_KEY")


@router.get("/follow/get")
async def get_followers_and_following(request: Request, id: int = None, authorization: Optional[str] = Header(None)):
    try:
        user_id = jwt.decode(authorization, secret_key, algorithms="HS256").get("id")
    except:
        return JSONResponse({'Error': 'Incorrect Authorization Token'}, status_code=401)
    user = None
    if id is None:
        user = await db_user.get_user(request.app.state.db, id=user_id)
        if user is None:
            return JSONResponse({'None': 'No user is authenticated'}, status_code=401)
    else:
        user = await db_user.get_user(request.app.state.db, id=id)
    data = await db_user.get_followers_and_following(request.app.state.db, user)
    return JSONResponse(data)


@router.post("/follow")
async def follow_user(request: Request, id: int, authorization: Optional[str] = Header(None)):
    try:
        user_id = jwt.decode(authorization, secret_key, algorithms="HS256").get("id")
    except:
        return JSONResponse({'Error': 'Incorrect Authorization Token'}, status_code=401)
    to_follow = await db_user.get_user(request.app.state.db, id=id)
    if to_follow is None:
        return JSONResponse({'Error': 'No such user exists'}, status_code=404)
    user = await db_user.get_user(request.app.state.db, id=user_id)
    if user is None:
        return JSONResponse({'None': 'No user is authenticated'}, status_code=401)
    current_following = json.loads(user.following)
    if id not in current_following and id != user.id:
        current_following.append(id)
    else:
        return JSONResponse({'Error': 'User already followed'}, status_code=400)
    new_following = list(set(current_following))
    await request.app.state.db.execute("UPDATE users SET following = $1 WHERE id = $2", json.dumps(new_following),
                                       user.id)
    current_followers = json.loads(to_follow.followers)
    if user.id not in current_followers and user.id != to_follow.id:
        print("Current Followers: ", current_followers)
        current_followers.append(user.id)
        print('id appended: ', id)
    else:
        return JSONResponse({'Error': 'User already followed'}, status_code=400)
    new_followers = list(set(current_followers))
    await request.app.state.db.execute("UPDATE users SET followers = $1 WHERE id = $2", json.dumps(new_followers),
                                       to_follow.id)
    return JSONResponse({'Success': f'{user.first_name} followed {to_follow.first_name}'},
                        status_code=200)


@router.post("/unfollow")
async def unfollow_user(request: Request, id: int, authorization: Optional[str] = Header(None)):
    try:
        user_id = jwt.decode(authorization, secret_key, algorithms="HS256").get("id")
    except:
        return JSONResponse({'Error': 'Incorrect Authorization Token'}, status_code=401)
    if user_id is None:
        return JSONResponse({'None': 'No user is authenticated'}, status_code=401)
    to_unfollow = await db_user.get_user(request.app.state.db, id=id)
    if to_unfollow is None:
        return JSONResponse({'Error': 'No such user exists'}, status_code=404)
    user = await db_user.get_user(request.app.state.db, id=user_id)
    if user is None:
        return JSONResponse({'None': 'No user is authenticated'}, status_code=401)
    current_following = json.loads(user.following)
    if id in current_following and id != user.id:
        current_following.remove(id)
    else:
        return JSONResponse({'Error': 'User not followed previously'}, status_code=400)
    new_following = list(set(current_following))
    await request.app.state.db.execute("UPDATE users SET following = $1 WHERE id = $2", json.dumps(new_following),
                                       user.id)

    current_followers = json.loads(to_unfollow.followers)
    if user.id in current_followers and user.id != to_unfollow.id:
        current_followers.remove(user.id)
    else:
        return JSONResponse({'Error': 'User already followed'}, status_code=400)
    new_followers = list(set(current_followers))
    await request.app.state.db.execute("UPDATE users SET followers = $1 WHERE id = $2", json.dumps(new_followers),
                                       to_unfollow.id)
    return JSONResponse({'Success': f'{user["first_name"]} unfollowed {to_unfollow["first_name"]}'},
                        status_code=200)
