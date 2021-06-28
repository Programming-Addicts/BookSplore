import json

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from database.utils import user as db_user

router = APIRouter(tags=["Follow Users"])


@router.get("/follow/get")
async def get_followers_and_following(request: Request, id: int = None):
    user = None
    if id is None:
        user = await db_user.get_user(request.app.state.db, session_id=request.cookies.get('session'))
        if user is None:
            return JSONResponse({'None': 'No user is authenticated'}, status_code=401)
    else:
        user = await db_user.get_user(request.app.state.db, id=id)
    data = await db_user.get_followers_and_following(request.app.state.db, user)
    return JSONResponse(data)


@router.patch("/follow")
async def follow_user(request: Request, id: int):
    to_follow = await db_user.get_user(request.app.state.db, id=id)
    if to_follow is None:
        return JSONResponse({'Error': 'No such user exists'}, status_code=404)
    user = await db_user.get_user(request.app.state.db, session_id=request.cookies.get('session'))
    if user is None:
        return JSONResponse({'None': 'No user is authenticated'}, status_code=401)
    current_following = json.loads(vars(user)['following'])
    if id not in current_following and id != vars(user)['id']:
        current_following.append(id)
    else:
        return JSONResponse({'Error': 'User already followed'}, status_code=400)
    new_following = list(set(current_following))
    await request.app.state.db.execute("UPDATE users SET following = $1 WHERE id = $2", json.dumps(new_following),
                                       vars(user)['id'])
    current_followers = json.loads(vars(to_follow)['followers'])
    if vars(user)['id'] not in current_followers and vars(user)['id'] != vars(to_follow)['id']:
        print("Current Followers: ", current_followers)
        current_followers.append(vars(user)['id'])
        print('id appended: ', id)
    else:
        return JSONResponse({'Error': 'User already followed'}, status_code=400)
    new_followers = list(set(current_followers))
    await request.app.state.db.execute("UPDATE users SET followers = $1 WHERE id = $2", json.dumps(new_followers),
                                       vars(to_follow)['id'])
    return JSONResponse({'Success': f'{vars(user)["first_name"]} followed {vars(to_follow)["first_name"]}'},
                        status_code=200)


@router.patch("/unfollow")
async def unfollow_user(request: Request, id: int):
    to_unfollow = await db_user.get_user(request.app.state.db, id=id)
    if to_unfollow is None:
        return JSONResponse({'Error': 'No such user exists'}, status_code=404)
    user = await db_user.get_user(request.app.state.db, session_id=request.cookies.get('session'))
    if user is None:
        return JSONResponse({'None': 'No user is authenticated'}, status_code=401)
    current_following = json.loads(vars(user)['following'])
    if id in current_following and id != vars(user)['id']:
        current_following.remove(id)
    else:
        return JSONResponse({'Error': 'User not followed previously'}, status_code=400)
    new_following = list(set(current_following))
    await request.app.state.db.execute("UPDATE users SET following = $1 WHERE id = $2", json.dumps(new_following),
                                       vars(user)['id'])

    current_followers = json.loads(vars(to_unfollow)['followers'])
    if vars(user)['id'] in current_followers and vars(user)['id'] != vars(to_unfollow)['id']:
        current_followers.remove(vars(user)['id'])
    else:
        return JSONResponse({'Error': 'User already followed'}, status_code=400)
    new_followers = list(set(current_followers))
    await request.app.state.db.execute("UPDATE users SET followers = $1 WHERE id = $2", json.dumps(new_followers),
                                       vars(to_unfollow)['id'])
    return JSONResponse({'Success': f'{vars(user)["first_name"]} unfollowed {vars(to_unfollow)["first_name"]}'},
                        status_code=200)
