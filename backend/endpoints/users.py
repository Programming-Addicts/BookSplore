from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from models.users import User
from database.utils.user import get_user

router = APIRouter(tags=["Users"])


@router.get('/current')
async def get_current_user(request: Request):
    user = await get_user(request.app.state.db, session_id=request.cookies.get('session'))
    if user is not None:
        return user
    else:
        return JSONResponse({'None': 'No user is authenticated'}, status_code=401)
