from datetime import datetime
from typing import List

from fastapi import FastAPI, HTTPException

app = FastAPI(title='Watt Next FastAPI Demo')


def _iso(dt: datetime) -> str:
    return dt.isoformat()


def _seed_articles() -> List[dict]:
    """
    Returns a deterministic list of article dictionaries used by the demo frontend.
    """
    now = datetime.utcnow()
    return [
        {
            'id': 1,
            'title': 'FastAPI Meets Watt',
            'slug': 'fastapi-meets-watt',
            'excerpt': 'Bringing Python services into the Watt runtime with the @platformatic/python stackable.',
            'content': '<p>FastAPI now runs side-by-side with Node.js inside Watt. This demo showcases how to compose a polyglot stack without leaving the Platformatic ecosystem.</p>',
            'author': 'Platformatic Team',
            'published': True,
            'published_at': _iso(now),
            'created_at': _iso(now),
            'updated_at': _iso(now),
        },
        {
            'id': 2,
            'title': 'Composing Services with Python',
            'slug': 'composing-services-with-python',
            'excerpt': 'Use Platformatic Composer to stitch FastAPI and Next.js together under one runtime.',
            'content': '<p>Composer lets you proxy requests between services without extra infrastructure. Requests to <code>/api</code> hit FastAPI directly, while the frontend stays on Next.js.</p>',
            'author': 'Platformatic Team',
            'published': True,
            'published_at': _iso(now),
            'created_at': _iso(now),
            'updated_at': _iso(now),
        },
        {
            'id': 3,
            'title': 'ASGI Inside Node.js',
            'slug': 'asgi-inside-nodejs',
            'excerpt': 'The embedded Python runtime keeps latency low and deployment simple.',
            'content': '<p>The <code>@platformatic/python</code> stackable embeds CPython inside Fastify, so FastAPI handlers execute in-process. That means fewer hops, less overhead, and unified configuration.</p>',
            'author': 'Platformatic Team',
            'published': True,
            'published_at': _iso(now),
            'created_at': _iso(now),
            'updated_at': _iso(now),
        },
    ]


ARTICLES: List[dict] = _seed_articles()


@app.get('/')
async def read_root():
    return {'message': 'FastAPI running inside Platformatic', 'articles_url': '/api/articles'}


@app.get('/articles')
async def list_articles():
    return {
        'data': ARTICLES,
        'current_page': 1,
        'last_page': 1,
        'per_page': len(ARTICLES),
        'total': len(ARTICLES),
    }


@app.get('/articles/{article_id}')
async def get_article(article_id: int):
    for article in ARTICLES:
        if article['id'] == article_id:
            return article

    raise HTTPException(status_code=404, detail='Article not found')
