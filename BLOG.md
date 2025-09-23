# FastAPI + Next.js: Running Python Inside Watt

The Watt runtime can now serve Python applications through the `@platformatic/python` stackable. That means you can wire FastAPI alongside your JavaScript services without leaving Node.js.

## Why It Matters

Mixing ecosystems usually means stitching together multiple deployment targets. With the Python stackable you can:

- Run FastAPI inside the same Watt process as your Node.js services
- Share configuration, logging, and orchestration across languages
- Keep latency low because requests never leave the runtime
- Prototype Python APIs without provisioning separate servers

## Getting Started: FastAPI in the Watt Runtime

This section walks through the structure used in `watt-next-fastapi`, but you can apply the same pattern to new projects.

### Prerequisites

- Node.js 22.14+
- Python 3.11+
- `fastapi` installed for the service (e.g. `pip install fastapi`)

### Step 1: Define Workspaces

`package.json`

```json
{
  "name": "watt-next-fastapi",
  "workspaces": [
    "web/*"
  ],
  "scripts": {
    "start": "wattpm start",
    "dev": "wattpm dev",
    "build": "wattpm build"
  },
  "dependencies": {
    "@platformatic/runtime": "^2.64.0",
    "platformatic": "^2.64.0",
    "wattpm": "^2.64.0"
  }
}
```

### Step 2: Create the FastAPI Workspace

`web/fastapi/package.json`

```json
{
  "name": "fastapi-service",
  "private": true,
  "type": "module",
  "scripts": {
    "start": "platformatic start"
  },
  "dependencies": {
    "@platformatic/python": "^0.7.0"
  }
}
```

`web/fastapi/platformatic.json`

```json
{
  "$schema": "https://schemas.platformatic.dev/@platformatic/python/0.7.0.json",
  "module": "@platformatic/python",
  "python": {
    "docroot": "public",
    "appTarget": "main:app"
  },
  "server": {
    "hostname": "{PLT_SERVER_HOSTNAME}",
    "port": "{PORT}",
    "logger": {
      "level": "{PLT_SERVER_LOGGER_LEVEL}"
    }
  },
  "watch": true
}
```

`web/fastapi/public/main.py`

```python
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Watt + FastAPI")

ARTICLES = [
    {
        "id": 1,
        "title": "FastAPI Meets Watt",
        "excerpt": "Bringing Python into the Watt runtime.",
        "content": "<p>FastAPI now runs side-by-side with Node.js inside Watt.</p>"
    }
]

@app.get('/api/articles')
async def list_articles():
    return {
        "data": ARTICLES,
        "current_page": 1,
        "last_page": 1,
        "per_page": len(ARTICLES),
        "total": len(ARTICLES)
    }

@app.get('/api/articles/{article_id}')
async def get_article(article_id: int):
    for article in ARTICLES:
        if article["id"] == article_id:
            return article
    raise HTTPException(status_code=404, detail="Article not found")
```

Install FastAPI inside the workspace (or a virtual environment):

```bash
cd web/fastapi
pip install fastapi
```

### Step 3: Route Traffic Through Composer

`web/composer/platformatic.json`

```json
{
  "composer": {
    "services": [
      { "id": "fastapi", "proxy": { "prefix": "/api" } },
      { "id": "my-app", "proxy": { "prefix": "/" } }
    ]
  }
}
```

Composer now fronts the entire stack: Next.js receives browser requests, while calls to `/api/**` land inside FastAPI running under Node.js.

## What You Get

- **Single runtime** – Watt hosts Next.js, Composer, and FastAPI in one process
- **ASGI compatibility** – Any ASGI framework (FastAPI, Starlette, Django Channels) can plug into the stackable
- **Polyglot productivity** – Pair Python data services with JavaScript UIs without extra infrastructure

## Next Steps

- Add persistence by wiring FastAPI handlers to your database of choice
- Generate OpenAPI documentation directly from FastAPI and expose it through Composer
- Extend the frontend to exercise new endpoints under `/api`

Check out `web/fastapi/public/main.py` for the full demo and `@platformatic/python`'s README for deeper configuration options.
