"""
Usage: `python scrub_notebook_solutions.py <input_file> <output_file>`
"""
import json
import sys


def main(path):
    """
    Clean Jupyter notebooks for sharing with students by clearing all
    outputs and the contents of any cell that has a "scrub" tag.
    """
    with open(path, 'r') as f:
        notebook = json.load(f)
    notebook["cells"] = [
        cell for cell in notebook["cells"] if cell["cell_type"] == "markdown"
    ]
    with open(path.replace(".ipynb", ".tmp.ipynb"), 'w') as f:
        f.write(json.dumps(notebook))


if __name__ == '__main__':
    main(path=sys.argv[1])
