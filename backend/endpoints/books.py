from fastapi import APIRouter, Request
import os
from aiohttp import request as aiorequest
import dotenv

dotenv.load_dotenv('.env')
api_key = os.environ.get('GOOGLE_API_KEY')
router = APIRouter(tags=["Books"])


@router.get('/books/search')
async def search(request: Request, query: str, limit: int = 20, download: bool = False, filter: str = None, sorting: str = "relevance"):
    url = 'https://www.googleapis.com/books/v1/volumes'
    params = {'key': api_key, 'q': query, 'maxResults': limit}

    if filter in ['partial', 'full', 'free-ebooks', 'paid-ebooks', 'ebooks']:
        params['filter'] = filter

    if download:
        params['download'] = 'epub'

    if sorting in ['relevance', 'newest']:
        params['orderBy'] = sorting

    async with aiorequest('GET', url, params=params) as response:
        data = await response.json()
        books = []
        for book in data['items']:

            book_info = book['volumeInfo']
            access_info = book['accessInfo']
            has_pdf = access_info.get('pdf')
            has_epub = access_info.get('epub')
            if download and not (has_epub['isAvailable'] == True) or (has_pdf['isAvailable'] == True) and len(has_epub.keys()) < 2 and len(has_pdf.keys()) < 2:
                continue
            book_data = {'id': book.get('id'),
                         'title': book_info.get('title'),
                         'authors': book_info.get('authors'),
                         'description': book_info.get('description'),
                         'publisher': book_info.get('publisher'),
                         'publish_date' : book_info.get('publishedDate'),
                         'isbns' : book_info.get('industryIdentifiers'),
                         'page_count': book_info.get('pageCount'),
                         'image_links': book_info.get('imageLinks'),
                         'preview_link': book_info.get('previewLink'),
                         'pdf': has_pdf,
                         'epub': has_epub
                         }
            books.append(book_data)

        return books



