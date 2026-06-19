# 01_imports - Different ways to import modules in Python

# Standard library import
import math
print("math.sqrt(16) =", math.sqrt(16))

# Import with alias
import datetime as dt
print("current year:", dt.date.today().year)

# Import specific names from a module
from random import randint, choice
print("random int 1-10:", randint(1, 10))
print("random choice:", choice(["apple", "banana", "cherry"]))

# Import everything (generally avoid in real code)
from os import getcwd  # noqa: F401
print("cwd:", getcwd())
