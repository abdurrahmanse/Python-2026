# 19 — Databases

Store and query data. SQL basics, the bundled `sqlite3` module, and an ORM with SQLAlchemy.

## Subfolders

1. `01_sql_basics/` — `SELECT`, `INSERT`, `UPDATE`, `DELETE`
2. `02_sqlite/` — Python's built-in `sqlite3` module
3. `03_orms/` — SQLAlchemy Core/ORM basics and Alembic migrations

## Setup

```bash
pip install -r requirements.txt
```

## Run them in order

```bash
for d in 0?_*/; do python3 "$d/app.py"; done
```

## Next

Move on to [`20_web_and_api`](../20_web_and_api).