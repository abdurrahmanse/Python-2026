# Python Learning Folder

A 21-topic Python curriculum. Each topic is a numbered folder, and inside each topic the work is split into numbered subfolders, each holding a small runnable example.

Start from `01_setup_and_basics` and move down in order.

## Folder Structure

```
python/
├── .gitignore
├── README.md
├── example.txt
├── 01_setup_and_basics/
├── 02_variables_and_data_types/
│   ├── 01_variables_and_data_types/
│   ├── 02_type_conversion/
│   └── 03_multiple_assignment_and_constants/
├── 03_operators_and_expressions/
│   ├── 01_arithmetic_operators/
│   ├── 02_comparison_operators/
│   ├── 03_logical_operators/
│   └── 04_assignment_operators/
├── 04_conditions/
├── 05_loops/
├── 06_functions/
├── 07_data_structures/
├── 08_strings/
├── 09_modules_and_packages/
│   ├── 01_imports/
│   ├── 02_creating_modules/
│   ├── 03_packages/
│   └── 04_project_structure/
├── 10_file_handling/
├── 11_errors_and_exceptions/
├── 12_oop/
├── 13_comprehensions_iterators_generators/
├── 14_decorators_context_managers/
├── 15_testing_debugging_logging/   # has requirements.txt
├── 16_standard_library/
├── 17_environment_and_packages/
├── 18_async_and_concurrency/       # has requirements.txt
├── 19_databases/                   # has requirements.txt
├── 20_web_and_api/                 # has requirements.txt
└── 21_projects_and_practice/       # has requirements.txt
```

## Learning Order

1. `01_setup_and_basics` — install Python, run scripts, syntax, comments, input/output
2. `02_variables_and_data_types` — variables, numbers, strings, booleans, type conversion, constants
3. `03_operators_and_expressions` — arithmetic, comparison, logical, assignment operators
4. `04_conditions` — `if`, `elif`, `else`, nested conditions, logical decisions
5. `05_loops` — `for`, `while`, nested loops, `break`, `continue`, `pass`
6. `06_functions` — defining functions, arguments, return values, scope, recursion, lambda
7. `07_data_structures` — lists, tuples, sets, dictionaries, nested structures, common methods
8. `08_strings` — string basics, slicing, methods, formatting
9. `09_modules_and_packages` — `import`, custom modules, `__init__.py`, project structure
10. `10_file_handling` — reading files, writing files, CSV, JSON
11. `11_errors_and_exceptions` — `try`, `except`, custom errors, `finally`, `assert`
12. `12_oop` — classes, objects, methods, inheritance, polymorphism, encapsulation, magic methods
13. `13_comprehensions_iterators_generators` — comprehensions, iterators, generators
14. `14_decorators_context_managers` — decorators and context managers
15. `15_testing_debugging_logging` — `pytest`, debugging, `logging`
16. `16_standard_library` — `os`, `pathlib`, `datetime`, `random`, `math`
17. `17_environment_and_packages` — virtual environments, pip, requirements files, package management
18. `18_async_and_concurrency` — `asyncio`, threads, processes
19. `19_databases` — SQL basics, SQLite, ORMs
20. `20_web_and_api` — HTTP basics, requests, REST, JSON, Flask/FastAPI
21. `21_projects_and_practice` — beginner, intermediate, advanced projects, challenges

Every topic folder has its own `README.md` with subfolder descriptions and the recommended run order.

## Setup

Requires Python 3.10 or newer. The first topics use only the standard library — no install needed. From topic 15 onwards some examples need third-party packages.

```bash
# 1. (Recommended) Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate          # macOS / Linux
# .venv\Scripts\activate           # Windows

# 2. Install dependencies for the topic you're on
cd 15_testing_debugging_logging && pip install -r requirements.txt && cd ..
cd 20_web_and_api               && pip install -r requirements.txt && cd ..
```

`requirements.txt` files live next to the topics that need them (15, 18, 19, 20, 21).

## How To Use

- Open the topic's `README.md` and follow the subfolder order it suggests.
- Run a single example: `python3 path/to/folder/app.py`
- Run every example in a topic (zsh/bash):

  ```bash
  for d in NN_topic/0?_*; do python3 "$d/app.py"; done
  ```

- **Keep one concept per file** when you add new examples.
- **Add more numbered folders** later if you want to split a topic further.

## Conventions

- Topic and subfolder names use `snake_case`.
- Topic folders are numbered `01_` … `21_` and are walked in that order.
- Subfolders inside a topic are numbered `01_`, `02_`, … and walked in that order.
- Every script is named `app.py` so a topic can be walked with a single `for` loop.
- Every runnable example is executable as `python3 app.py` from its own folder.
