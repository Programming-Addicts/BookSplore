import json

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from database.utils import user as db_user

router = APIRouter(tags=["Follow Users"])

@router.get("/follow/get")
async def get_followers_and_following(request: Request, id:int = None):
    user = None
    if id is None:
        req_user = request.session.get('user')
        user = await db_user.get_user(request.app.state.db, email=req_user['email'])
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
        return JSONResponse({'Error' : 'No such user exists'}, status_code=404)
    req_user = request.session.get('user')
    user = await db_user.get_user(request.app.state.db, email=req_user['email'])
    if user is None:
        return JSONResponse({'None': 'No user is authenticated'}, status_code=401)
    current_following = json.loads(vars(user)['following'])
    print(vars(user),vars(to_follow), sep="\n\n\n\n")
    if id not in current_following and id != vars(user)['id']:
        current_following.append(id)
    else:
        return JSONResponse({'Error': 'User already followed'}, status_code=400)
    new_following = list(set(current_following))
    await request.app.state.db.execute("UPDATE users SET following = $1 WHERE id = $2", json.dumps(new_following), vars(user)['id'])
    current_followers = json.loads(vars(to_follow)['followers'])
    if vars(user)['id'] not in current_followers and vars(user)['id'] != vars(to_follow)['id']:
        current_followers.append(id)
    else:
        return JSONResponse({'Error' : 'User already followed'}, status_code=400)
    new_followers = list(set(current_followers))
    await request.app.state.db.execute("UPDATE users SET followers = $1 WHERE id = $2", json.dumps(new_followers), vars(to_follow)['id'])
    return JSONResponse({'Success': f'{vars(user)["first_name"]} followed {vars(to_follow)["first_name"]}'}, status_code=200)

@router.patch("/unfollow")
async def unfollow_user(request: Request, id: int):
    pass

@router.get("/get-followers")
async def get_followers(request: Request, id: int):
    pass

async def get_following(request: Request, id: int):
    pass