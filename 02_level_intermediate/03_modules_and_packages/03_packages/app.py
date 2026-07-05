# 03_packages - A package is a folder of modules with an __init__.py.
#
# This example uses the `my_package/` sibling folder, which contains:
#   my_package/__init__.py
#   my_package/operations.py
#
# Run from inside this folder:
#   cd 09_modules_and_packages/03_packages
#   python3 app.py
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from my_package import add, multiply  # noqa: E402

print("add(2, 3) =", add(2, 3))
print("multiply(4, 5) =", multiply(4, 5))
