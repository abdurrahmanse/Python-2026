# 09 — Modules and Packages

Organize code across files and folders. Import the standard library, build your own modules, and package them.

## Subfolders

1. `01_imports/` — `import`, `from … import …`, aliases, `sys.path`
2. `02_creating_modules/` — writing your own `.py` modules
3. `03_packages/` — `__init__.py` and sub-packages (see `my_package/`)
4. `04_project_structure/` — typical `src/` + `tests/` + `pyproject.toml` layout

## Run them in order

```bash
cd 01_imports           && python3 app.py && cd ..
cd 02_creating_modules  && python3 app.py && cd ..
cd 03_packages          && python3 app.py && cd ..
cd 04_project_structure && python3 app.py && cd ..
```

## Next

Move on to [`10_file_handling`](../10_file_handling).