"""
The functions to test EOS devices are coded in the module "tests" in the package "nta"
These functions have docstrings.
This script uses the docstrings to generate the functions documentation in markdown format.
The generated markdown documentation is in the directory "documentation".
"""

from lazydocs import generate_docs

generate_docs(["nta.tests"], output_path="./documentation", overview_file = 'overview.md')
