"""
Usage: python scrub_notebook_scrubs.py <input_file> <output_file> <input_file_asset_relpath> <output_file_asset_relpath>

where `input_file_asset_relpath` is the relative path from the input
file to a directory containing assets (e.g. images) and
`output_file_asset_relpath` is the relative path from the output file
file to the same directory.

Cleans Jupyter notebooks for sharing with students:

- Clears outputs of all cells.
- Clears contents of any cell that contains "/scrub/" from the line that
contains it onwards. The idea is that you will mark cell contents that
you don't want to share with students (e.g. solution code) with the
comment "# /scrub/".
"""
# coding: utf-8
import json
import sys


def main(input_file, output_file):
    with open(input_file, 'r') as f:
        notebook = json.load(f)
    for cell in notebook['cells']:
        cell = _clear_outputs(cell)
        scrub_line_num = _get_scrub_comment_line_num(cell)
        if scrub_line_num is not None:
            cell = _clear_source_from_line(cell, scrub_line_num)
    with open(output_file, 'w') as f:
        f.write(json.dumps(notebook))


def _clear_outputs(cell):
    if 'execution_count' in cell:
        cell['execution_count'] = None
    if 'outputs' in cell:
        cell['outputs'] = []
    return cell


def _get_scrub_comment_line_num(cell):
    scrub_line_num = None
    for line_num, line in enumerate(cell['source']):
        if '/scrub/' in line:
            scrub_line_num = line_num
            break
    return scrub_line_num


def _clear_source_from_line(cell, line_num):
    cell['source'] = cell['source'][:line_num]
    return cell


if __name__ == '__main__':
    INPUT_FILE, OUTPUT_FILE = sys.argv[1:]
    main(INPUT_FILE, OUTPUT_FILE)
