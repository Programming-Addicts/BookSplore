from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from models.users import User
from database.utils.user import get_user

router = APIRouter(tags=["Users"])

@router.get('/users/current')
async def get_current_user(request: Request):
    user_data = request.session.get('user')
    if user_data is None:
        return JSONResponse({'None': 'No user is authenticated'}, status_code=401)
    user = await get_user(request.app.state.db, email=user_data['email'])
    if user is not None:
        return user
    else:
        return JSONResponse({'None': 'No user is authenticated'}, status_code=401)