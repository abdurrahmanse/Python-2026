# Python Learning Curriculum

A hands-on Python curriculum organized by difficulty level. Each level holds numbered topics, and each topic holds numbered subfolders with a small runnable `app.py`.

Work through the levels in order: **beginner → intermediate → advanced → projects**.

## Folder Structure

```
python/
├── .gitignore
├── README.md
├── data/                              # shared sample data used by some examples
├── 01_beginner/
│   ├── 01_setup_and_basics/
│   ├── 02_variables_and_data_types/
│   ├── 03_operators_and_expressions/
│   ├── 04_conditions/
│   ├── 05_loops/
│   ├── 06_strings/
│   └── 07_functions/
├── 02_intermediate/
│   ├── 01_data_structures/
│   ├── 02_functions_advanced/         # decorators, context managers
│   ├── 03_modules_and_packages/       # includes 05_environment_setup/
│   ├── 04_file_handling/
│   ├── 05_errors_and_exceptions/
│   ├── 06_oop/
│   ├── 07_comprehensions_generators/
│   └── 08_standard_library/
├── 03_advanced/
│   ├── 01_testing/                    # testing, debugging, logging — has requirements.txt
│   ├── 02_async_concurrency/          # has requirements.txt
│   ├── 03_databases/                  # has requirements.txt
│   └── 04_web_and_api/                # has requirements.txt
└── 04_projects/                       # beginner → advanced projects + challenges — has requirements.txt
```

## Learning Path

### 01_beginner
1. `01_setup_and_basics` — install Python, run scripts, `print()`, comments, `input()`
2. `02_variables_and_data_types` — variables, numbers, strings, booleans, type conversion, constants
3. `03_operators_and_expressions` — arithmetic, comparison, logical, assignment operators
4. `04_conditions` — `if`, `elif`, `else`, nested conditions
5. `05_loops` — `for`, `while`, nested loops, `break`, `continue`, `pass`
6. `06_strings` — string basics, slicing, methods, formatting
7. `07_functions` — defining functions, arguments, return values, scope, recursion, lambda

### 02_intermediate
1. `01_data_structures` — lists, tuples, sets, dictionaries, nested structures, common methods
2. `02_functions_advanced` — decorators and context managers
3. `03_modules_and_packages` — `import`, custom modules, packages, project structure, environment setup
4. `04_file_handling` — reading files, writing files, CSV, JSON
5. `05_errors_and_exceptions` — `try`, `except`, custom errors, `finally`, `assert`
6. `06_oop` — classes, inheritance, polymorphism, encapsulation, magic methods
7. `07_comprehensions_generators` — comprehensions, iterators, generators
8. `08_standard_library` — `os`, `pathlib`, `datetime`, `random`, `math`

### 03_advanced
1. `01_testing` — `pytest`, debugging, `logging`
2. `02_async_concurrency` — `asyncio`, threads, processes
3. `03_databases` — SQL basics, SQLite, ORMs
4. `04_web_and_api` — HTTP basics, `requests`, REST, JSON, Flask/FastAPI

### 04_projects
Hands-on projects grouped by difficulty, plus algorithm challenges.

Every topic folder has its own `README.md` describing its subfolders and a suggested run order, with a "Next" link to the following topic.

## Setup

Requires Python 3.10 or newer. The early topics use only the standard library — no install needed. Some advanced topics and the projects need third-party packages.

```bash
# 1. (Recommended) Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate          # macOS / Linux
# .venv\Scripts\activate           # Windows

# 2. Install dependencies for the topic you're on
pip install -r 03_advanced/01_testing/requirements.txt
pip install -r 03_advanced/04_web_and_api/requirements.txt
```

`requirements.txt` files live next to the topics that need them (all of `03_advanced/` and `04_projects/`).

## How To Use

- Open a topic's `README.md` and follow the subfolder order it suggests.
- Run a single example: `python3 path/to/subfolder/app.py`
- Run every example in a topic (zsh/bash):

  ```bash
  for d in 0?_*/; do python3 "$d/app.py"; done
  ```

## Conventions

- Level, topic, and subfolder names use `snake_case`.
- Levels are numbered `01_`…`04_`; topics and subfolders are numbered `01_`, `02_`, … and walked in that order.
- Every script is named `app.py` so a topic can be walked with a single `for` loop.
- Keep one concept per file; add more numbered subfolders to split a topic further.
