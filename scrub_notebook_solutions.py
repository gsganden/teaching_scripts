"""
Usage: python scrub_notebook_scrubs.py <input_file> <output_file> <input_file_asset_relpath> <output_file_asset_relpath>

where `input_file_asset_relpath` is the relative path from the input
file to a directory containing assets (e.g. images) and
`output_file_asset_relpath` is the relative path from the output file
file to the same directory.

Cleans Jupyter notebooks for sharing with students:

- Clears outputs of all cells.
- For every cells that contain a line that starts with # and contains
the word "scrub," deletes the content of that cell from that line
onward. The idea is that you will develop a notebook that contains
e.g. solution code that you don't want to share with students, putting
the comment "# scrub" above any lines that you don't want to share.
- Updates relative paths to assets. For instance, I put the instructor
version of the notebook in an `instructor_notes` directory, the student
version in the parent directory, and e.g. images that are embedded into
the notebook into an `assets` directory. As a result, paths to assets in
the instructor version of the notebook start with `../assets`, while
the corresponding paths in the sturdent version need to omit the `../`.
I run this script with `../assets` and `assets` as the last two
command-line arguments, and it simply replace any instances of the
former with the latter.
"""
# coding: utf-8
import json
import sys


def main(input_file, output_file):
    with open(input_file, 'r') as f:
        notebook = json.load(f)
    for cell in notebook['cells']:
        cell = _clear_outputs(cell)
        cell = _update_asset_paths(cell)
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


def _update_asset_paths(cell):
    for line_num, line in enumerate(cell['source']):
        cell['source'][line_num] = (
            line.replace(INPUT_ASSET_DIR_RELPATH, OUTPUT_ASSET_DIR_RELPATH)
            )
    return cell


def _get_scrub_comment_line_num(cell):
    scrub_line_num = None
    for line_num, line in enumerate(cell['source']):
        if line.startswith('#') and 'scrub' in line:
            scrub_line_num = line_num
            break
    return scrub_line_num


def _clear_source_from_line(cell, line_num):
    cell['source'] = cell['source'][:line_num]
    return cell


if __name__ == '__main__':
    INPUT_FILE, OUTPUT_FILE, INPUT_ASSET_DIR_RELPATH, OUTPUT_ASSET_DIR_RELPATH\
        = sys.argv[1:]
    main(INPUT_FILE, OUTPUT_FILE)
