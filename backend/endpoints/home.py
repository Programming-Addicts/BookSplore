from fastapi.responses import RedirectResponse
from fastapi import APIRouter, Request
router = APIRouter(tags=["Homepage"])


@router.get('/')
def home():
    return RedirectResponse("https://booksplore.netlify.app")
