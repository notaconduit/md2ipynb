"""
Markdown to Jupyter Notebook Converter.

A Python tool to convert Markdown files to Jupyter Notebooks.
"""

__version__ = "0.1.1"

from .main import convert_to_ipynb

__all__ = ["convert_to_ipynb"]

def hello() -> str:
    return "Hello from md2ipynb!"
