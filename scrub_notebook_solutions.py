"""
Usage: python scrub_notebook_solutions.py <input_file> <output_file>

Clears outputs of all cells in iPython notebook input file. Also clears
contents of any cells that begin with # and contain "solution." The idea
is that you will initially develop a notebook that contains solutuions
to exercises, with `# solution` as the first lines in those cells, and
then run this script to produce a version of that notebook for sharing
with students.
"""
# coding: utf-8
import json
import sys


def main(input_file, output_file):
    with open(input_file, 'r') as f:
        notebook = json.load(f)
    for cell in notebook['cells']:
        cell = _clear_outputs(cell)
        if _is_solution(cell):
            cell = _clear_source(cell)
    with open(output_file, 'w') as f:
        f.write(json.dumps(notebook))


def _clear_outputs(cell):
    if 'execution_count' in cell:
        cell['execution_count'] = None
    if 'outputs' in cell:
        cell['outputs'] = []
    return cell


def _is_solution(cell):
    source_first_line = cell['source'][0]
    first_line_is_comment = source_first_line.startswith('#')
    return first_line_is_comment and 'solution' in source_first_line


def _clear_source(cell):
    if 'source' in cell:
        cell['source'] = []
    return cell


if __name__ == '__main__':
    INPUT_FILE, OUTPUT_FILE = sys.argv[1:]
    main(INPUT_FILE, OUTPUT_FILE)
