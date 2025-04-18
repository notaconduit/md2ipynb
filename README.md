# Markdown2Ipynb

A Python tool to convert Markdown files to Jupyter Notebooks.

## Features

- Convert Markdown files to Jupyter Notebooks
- Automatically handle code blocks as executable cells
- Preserve formatting and structure from Markdown
- Command-line interface for easy use
- Python API for programmatic usage

## Requirements

- Python 3.8 or higher
- `pypandoc` and `nbformat` libraries

## Installation

You can install directly from PyPI:

```sh
pip install md2ipynb
```

Or from source:

```sh
git clone https://github.com/yourusername/md2ipynb.git
cd md2ipynb
pip install .
```

## Usage

### Command Line Interface

Convert a Markdown file to a Jupyter Notebook:

```sh
md2ipynb input.md output.ipynb
```

If you don't specify an output file, it will use the input filename with an `.ipynb` extension:

```sh
md2ipynb input.md
# Creates input.ipynb
```

Use the `--verbose` flag for more detailed output:

```sh
md2ipynb input.md --verbose
```

### Python API

```python
from md2ipynb import convert_to_ipynb

# Convert a Markdown file to a Jupyter Notebook
result = convert_to_ipynb("input.md", "output.ipynb", verbose=True)

if result:
    print(f"Successfully converted to {result}")
else:
    print("Conversion failed")
```

## Development

### Setup Development Environment

```sh
# Clone the repository
git clone https://github.com/yourusername/md2ipynb.git
cd md2ipynb

# Install development dependencies
pip install -e ".[dev]"
```

### Running Tests

```sh
# Run all tests
pytest

# Run tests with coverage
pytest --cov=src/md2ipynb

# Run specific tests
pytest tests/test_conversion.py
```

### Code Quality

```sh
# Format code
black src/ tests/

# Sort imports
isort src/ tests/

# Run linter
flake8 src/ tests/

# Type checking
mypy src/ tests/
```

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

 --------
