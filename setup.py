"""Setup script for md2ipynb package."""

import os
from setuptools import setup, find_packages

# Get version from package
with open(os.path.join("src", "md2ipynb", "__init__.py"), "r") as f:
    for line in f:
        if line.startswith("__version__"):
            version = line.split("=")[1].strip().strip('"').strip("'")
            break
    else:
        version = "0.1.1"  # Fallback version

# Read long description from README.md
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="md2ipynb",
    version=version,
    description="A Python Tool to Convert Markdown Files to Jupyter Notebooks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="notaconduit",
    author_email="email@email",
    url="https://github.com/notaconduit/md2ipynb",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[
        "pypandoc>=1.15",
        "nbformat>=5.10.4",
    ],
    entry_points={
        "console_scripts": [
            "md2ipynb=md2ipynb.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Markup :: Markdown",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.3.0",
            "isort>=5.12.0",
            "flake8>=6.0.0",
            "mypy>=1.3.0",
        ],
    },
) 