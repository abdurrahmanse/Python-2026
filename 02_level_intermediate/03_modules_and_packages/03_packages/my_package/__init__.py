"""my_package - example of a Python package.

Re-exporting names from submodules at the package root is a common
idiom so users can write `from my_package import add` instead of
`from my_package.operations import add`.
"""

from .operations import add, multiply  # noqa: F401

__all__ = ["add", "multiply"]
