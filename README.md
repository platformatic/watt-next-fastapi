# Watt Next FastAPI

A full-stack demo that pairs a Next.js frontend with a FastAPI backend, all orchestrated by Platformatic Watt.

## Project Structure

This workspace bundles three services:

- **`web/my-app`** – Next.js 15 + React 19 frontend styled with Tailwind CSS
- **`web/fastapi`** – FastAPI application served through the `@platformatic/python` stackable
- **`web/composer`** – Platformatic Composer entrypoint that proxies `/` to Next.js and `/api` to FastAPI

## Prerequisites

- Node.js >= 22.14.0
- Python >= 3.11
- Python dependencies installed with `pip install -r web/fastapi/requirements.txt`

Copy the sample environment to configure Watt:

```bash
cp .env.sample .env
```

The defaults expose the runtime on `http://127.0.0.1:3042`.

## Installation

Install JavaScript dependencies across all workspaces:

```bash
npm install
```

(Optional) Create a Python virtual environment for the FastAPI backend:

```bash
cd web/fastapi
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd ../..
```

## Development

Start all services with hot reload:

```bash
npm run dev
```

Composer will proxy frontend requests to Next.js and API traffic under `/api` to FastAPI.

## Production

Build every service:

```bash
npm run build
```

Then boot the stack:

```bash
npm start
```

## Services

### Frontend (Next.js)
- **Location**: `web/my-app/`
- **Endpoints**: Served at `/`
- **Responsibilities**: Renders the blog UI and fetches posts from the `/api` proxy

### Backend (FastAPI)
- **Location**: `web/fastapi/`
- **Endpoints**: `/api/articles`, `/api/articles/:id`
- **Responsibilities**: Supplies blog content through an in-memory catalog of articles

### Composer
- **Location**: `web/composer/`
- **Purpose**: Service orchestration and API composition
- **Endpoints**: Exposes the combined application on `http://127.0.0.1:{PORT}`

## Configuration

Key configuration lives in:

- `watt.json` – Watt runtime configuration
- `web/**/platformatic.json` – Service-specific Platformatic configs
- `.env` – runtime environment values

## Scripts

- `npm run dev` – Start development environment
- `npm run build` – Build all services
- `npm start` – Start production environment

## Architecture

Platformatic Watt loads each workspace automatically:

1. Composer receives incoming traffic
2. Requests to `/` render the Next.js frontend
3. Requests to `/api/**` execute inside FastAPI via the embedded Python runtime

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.
