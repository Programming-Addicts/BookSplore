from starlette.responses import HTMLResponse
from fastapi import APIRouter, Request
router = APIRouter(tags=["Homepage"])

@router.get('/')
async def home(request: Request):
    user = request.session.get('user')
    if user is not None:
        email = user['email']
        avatar_url = user['avatar_url']
        first_name = user['first_name']
        last_name = user['last_name']

        html = (
            f'<pre>First Name: {first_name}</pre><br>'
            f'<pre>Last Name: {last_name}</pre><br>'
            f'<pre>Email: {email}</pre><br>'
            f'<pre><img src="{avatar_url}" alt="Profile Picture"></pre><br>'
            '<a href="/logout">logout</a>'
        )
        return HTMLResponse(html)
    return HTMLResponse('<a href="/login">login</a>')