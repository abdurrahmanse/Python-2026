# 04_project_structure - Typical Python project layout.
#
# Real projects usually look like this:
#
#   my_project/
#   ├── pyproject.toml          # build + dependency metadata (PEP 621)
#   ├── README.md
#   ├── .gitignore
#   ├── src/
#   │   └── my_project/
#   │       ├── __init__.py
#   │       └── core.py
#   ├── tests/
#   │   └── test_core.py
#   └── scripts/
#       └── run_demo.py
#
# Why this layout?
#   * `src/` prevents accidental imports from the working directory.
#   * `tests/` mirrors the package layout for easy discovery.
#   * `pyproject.toml` is the modern single source of truth for
#     build, dependencies, and tool config (pytest, ruff, mypy, ...).
#
# This file just prints the tree as a reminder. There is nothing to run.

TREE = """
my_project/
├── pyproject.toml
├── README.md
├── .gitignore
├── src/
│   └── my_project/
│       ├── __init__.py
│       └── core.py
├── tests/
│   └── test_core.py
└── scripts/
    └── run_demo.py
"""

if __name__ == "__main__":
    print(TREE)
