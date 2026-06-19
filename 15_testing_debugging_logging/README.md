# 15 — Testing, Debugging, Logging

Write tests with `pytest`, debug with `pdb`/`breakpoint()`, and produce structured logs.

## Subfolders

1. `01_testing/` — `pytest` test functions and assertions
2. `02_debugging/` — `breakpoint()`, stepping through code
3. `03_logging/` — the `logging` module, levels, formatters

## Setup

```bash
pip install -r requirements.txt
```

## Run them in order

```bash
cd 01_testing          && pytest -q && cd ..
python3 02_debugging/app.py
python3 03_logging/app.py
```

## Next

Move on to [`16_standard_library`](../16_standard_library).