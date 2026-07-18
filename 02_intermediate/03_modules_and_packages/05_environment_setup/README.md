# Environment and Packages

Manage isolated environments with `venv`, install packages with `pip`, and pin dependencies in `requirements.txt`.

## Subfolders

1. `01_virtualenv/` — `python3 -m venv .venv`
2. `02_pip/` — installing, upgrading, uninstalling
3. `03_requirements/` — `pip freeze`, `pip install -r requirements.txt`
4. `04_package_management/` — `pyproject.toml` basics, dependency groups

## Run them in order

```bash
for d in 0?_*/; do python3 "$d/app.py"; done
```

## Next

Back to [`03_modules_and_packages`](../).