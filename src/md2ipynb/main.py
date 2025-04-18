import argparse
import logging
import os
import sys
from pathlib import Path
from typing import Optional

import nbformat
import pypandoc

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("md2ipynb")

def convert_to_ipynb(input_file: str, output_file: str, verbose: bool = False) -> Optional[str]:
    """
    Converts a Markdown file to a Jupyter Notebook file using pypandoc and nbformat.
    
    Args:
        input_file: Path to the input Markdown file
        output_file: Path to the output Jupyter Notebook file
        verbose: Whether to enable verbose output
        
    Returns:
        The path to the output file if successful, None otherwise
    """
    try:
        input_path = Path(input_file)
        output_path = Path(output_file)
        
        if not input_path.exists():
            logger.error(f"Input file '{input_file}' does not exist")
            return None
        
        if not input_path.is_file():
            logger.error(f"Input path '{input_file}' is not a file")
            return None
            
        # Create output directory if it doesn't exist
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        if verbose:
            logger.info(f"Converting '{input_file}' to '{output_file}'")
        
        # Convert the Markdown file to a Jupyter Notebook
        notebook = pypandoc.convert_file(
            str(input_path),
            "ipynb",
            extra_args=["--wrap=none"]
        )
        
        # Parse the notebook JSON
        nb = nbformat.reads(notebook, as_version=4)
        
        # Write the notebook to file
        nbformat.write(nb, str(output_path))
        
        if verbose:
            logger.info(f"Successfully converted to {output_file}")
        
        return output_file
        
    except Exception as e:
        logger.error(f"Error converting file: {str(e)}")
        return None

def main() -> int:
    """
    Main function to convert a Markdown file to a Jupyter Notebook file.
    
    Returns:
        Exit code (0 for success, 1 for error)
    """
    parser = argparse.ArgumentParser(
        description="Convert Markdown files to Jupyter Notebooks",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument(
        "input_file", 
        help="Path to the input Markdown file"
    )
    parser.add_argument(
        "output_file", 
        help="Path to the output Jupyter Notebook file",
        nargs="?",
        default=None
    )
    parser.add_argument(
        "-v", "--verbose", 
        action="store_true", 
        help="Enable verbose output"
    )
    parser.add_argument(
        "--version", 
        action="version", 
        version="%(prog)s 0.1.1"
    )
    
    args = parser.parse_args()
    
    # If output_file is not provided, use the input filename with .ipynb extension
    if args.output_file is None:
        input_path = Path(args.input_file)
        args.output_file = str(input_path.with_suffix(".ipynb"))
    
    result = convert_to_ipynb(args.input_file, args.output_file, args.verbose)
    
    return 0 if result else 1

if __name__ == "__main__":
    sys.exit(main())
 