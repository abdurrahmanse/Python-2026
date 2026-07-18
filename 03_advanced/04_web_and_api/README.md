# 04 — Web and API

Talk to HTTP services, build REST APIs, parse JSON, and serve a tiny app with Flask or FastAPI.

## Subfolders

1. `01_http_basics/` — methods, status codes, headers
2. `02_requests/` — the `requests` library
3. `03_rest_api/` — designing REST endpoints
4. `04_json/` — the `json` module end-to-end
5. `05_fastapi_flask/` — minimal Flask and FastAPI apps

## Setup

```bash
pip install -r requirements.txt
```

## Run them in order

```bash
for d in 0?_*/; do python3 "$d/app.py"; done
# For the web frameworks:
#   cd 05_fastapi_flask && uvicorn flask_demo:app --reload
```

## Next

You've finished the advanced level. Put it all together in [`04_projects`](../../04_projects).