# 02_creating_modules - Any .py file is a module you can import.
#
# This file demonstrates the concept by importing a sibling module
# called `greetings.py` (a tiny file in the same folder).

# Run this from inside this folder:
#   cd 09_modules_and_packages/02_creating_modules
#   python3 app.py
import sys
import os

# Make sure the current folder is on sys.path so `greetings` is importable
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import greetings  # noqa: E402

print(greetings.say_hello("World"))
print(greetings.say_goodbye("World"))
