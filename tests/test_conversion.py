"""Tests for the Markdown to Jupyter Notebook conversion functionality."""

import os
import tempfile
from pathlib import Path
import unittest

import nbformat

from src.md2ipynb.main import convert_to_ipynb


class TestConversion(unittest.TestCase):
    """Test cases for the Markdown to Jupyter Notebook conversion functionality."""

    def setUp(self):
        """Set up test fixtures."""
        # Create a temporary directory for test files
        self.test_dir = tempfile.TemporaryDirectory()
        self.test_dir_path = Path(self.test_dir.name)
        
        # Create a sample markdown file
        self.markdown_content = """# Test Markdown
        
This is a test markdown file.

```python
print("Hello, World!")
```

## Section 2

And some more text.
"""
        self.markdown_file = self.test_dir_path / "test.md"
        with open(self.markdown_file, "w") as f:
            f.write(self.markdown_content)
            
        # Output file path
        self.output_file = self.test_dir_path / "test.ipynb"

    def tearDown(self):
        """Clean up test fixtures."""
        self.test_dir.cleanup()

    def test_convert_to_ipynb_success(self):
        """Test successful conversion from Markdown to Jupyter Notebook."""
        result = convert_to_ipynb(
            str(self.markdown_file),
            str(self.output_file),
            verbose=True
        )
        
        # Check that the conversion was successful
        self.assertIsNotNone(result)
        self.assertEqual(result, str(self.output_file))
        
        # Check that the output file exists
        self.assertTrue(self.output_file.exists())
        
        # Verify the notebook content
        with open(self.output_file, "r") as f:
            notebook = nbformat.read(f, as_version=4)
            
        # Check that the notebook has cells
        self.assertGreater(len(notebook.cells), 0)
        
        # Check that the code block is converted to a code cell
        code_cells = [cell for cell in notebook.cells if cell.cell_type == "code"]
        self.assertGreaterEqual(len(code_cells), 1)
        
        # Check that at least one code cell contains our code
        found_code = False
        for cell in code_cells:
            if 'print("Hello, World!")' in cell.source:
                found_code = True
                break
        self.assertTrue(found_code)

    def test_convert_to_ipynb_nonexistent_file(self):
        """Test conversion with a nonexistent input file."""
        nonexistent_file = self.test_dir_path / "nonexistent.md"
        result = convert_to_ipynb(
            str(nonexistent_file),
            str(self.output_file)
        )
        
        # Check that the conversion failed
        self.assertIsNone(result)
        
        # Check that the output file doesn't exist
        self.assertFalse(self.output_file.exists())

    def test_convert_to_ipynb_invalid_input(self):
        """Test conversion with an invalid input file (directory instead of file)."""
        # Try to convert a directory
        result = convert_to_ipynb(
            str(self.test_dir_path),
            str(self.output_file)
        )
        
        # Check that the conversion failed
        self.assertIsNone(result)
        
        # Check that the output file doesn't exist
        self.assertFalse(self.output_file.exists())


if __name__ == "__main__":
    unittest.main() 