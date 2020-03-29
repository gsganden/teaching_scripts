"""
Usage: `python scrub_notebook_solutions.py <input_file> <output_file>`
"""
import json
import sys


def main(input_file, output_file):
    """
    Clean Jupyter notebooks for sharing with students by clearing all
    outputs and the contents of any cell that has a "scrub" tag.
    """
    with open(input_file, 'r') as f:
        notebook = json.load(f)
    for cell in notebook['cells']:
        cell = _clear_outputs(cell)
        if 'scrub' in cell['metadata'].get('tags', []):
            cell['source'] = []
    with open(output_file, 'w') as f:
        f.write(json.dumps(notebook))


def _clear_outputs(cell):
    if 'execution_count' in cell:
        cell['execution_count'] = None
    if 'outputs' in cell:
        cell['outputs'] = []
    return cell


if __name__ == '__main__':
    input_file, output_file = sys.argv[1:]
    main(input_file=input_file, output_file=output_file)
