"""Tests for the command-line interface."""

import os
import subprocess
import sys
import tempfile
from pathlib import Path
import unittest

class TestCLI(unittest.TestCase):
    """Test cases for the command-line interface."""

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
        
        # Path to the md2ipynb module
        self.module_path = "src.md2ipynb.main"

    def tearDown(self):
        """Clean up test fixtures."""
        self.test_dir.cleanup()

    def test_cli_success(self):
        """Test successful CLI conversion from Markdown to Jupyter Notebook."""
        # Run the CLI command
        result = subprocess.run(
            [
                sys.executable, 
                "-m", 
                self.module_path,
                str(self.markdown_file),
                str(self.output_file),
                "--verbose"
            ],
            capture_output=True,
            text=True
        )
        
        # Check that the command succeeded
        self.assertEqual(result.returncode, 0, 
                         f"CLI command failed with: {result.stderr}")
        
        # Check that the output file exists
        self.assertTrue(self.output_file.exists())
        
    def test_cli_auto_output_name(self):
        """Test CLI conversion with automatic output file name generation."""
        expected_output = self.markdown_file.with_suffix(".ipynb")
        
        # Make sure the expected output doesn't exist before the test
        if expected_output.exists():
            os.unlink(expected_output)
        
        # Run the CLI command without specifying output file
        result = subprocess.run(
            [
                sys.executable, 
                "-m", 
                self.module_path,
                str(self.markdown_file)
            ],
            capture_output=True,
            text=True
        )
        
        # Check that the command succeeded
        self.assertEqual(result.returncode, 0, 
                         f"CLI command failed with: {result.stderr}")
        
        # Check that the automatically named output file exists
        self.assertTrue(expected_output.exists())
        
        # Clean up the auto-generated file
        os.unlink(expected_output)
        
    def test_cli_invalid_input(self):
        """Test CLI conversion with a nonexistent input file."""
        nonexistent_file = self.test_dir_path / "nonexistent.md"
        
        # Run the CLI command
        result = subprocess.run(
            [
                sys.executable, 
                "-m", 
                self.module_path,
                str(nonexistent_file),
                str(self.output_file)
            ],
            capture_output=True,
            text=True
        )
        
        # Check that the command failed
        self.assertNotEqual(result.returncode, 0)
        
        # Check that the output file doesn't exist
        self.assertFalse(self.output_file.exists())


if __name__ == "__main__":
    unittest.main() 