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
    for cell in notebook['cells']:
        scrub_line_num = _get_scrub_comment_line_num(cell)
        if scrub_line_num is not None:
            _remove_line(cell, scrub_line_num)
            if 'tags' in cell['metadata']:
                cell['metadata']['tags'].append('scrub')
            else:
                cell['metadata']['tags'] = ['scrub']
    with open(path, 'w') as f:
        f.write(json.dumps(notebook))


def _get_scrub_comment_line_num(cell):
    scrub_line_num = None
    for line_num, line in enumerate(cell['source']):
        if '/scrub/' in line:
            scrub_line_num = line_num
            break
    return scrub_line_num


def _remove_line(cell, line_num):
    cell['source'] = cell['source'][:line_num] + cell['source'][line_num + 1 :]


def _clear_outputs(cell):
    if 'execution_count' in cell:
        cell['execution_count'] = None
    if 'outputs' in cell:
        cell['outputs'] = []
    return cell


if __name__ == '__main__':
    input_file, output_file = sys.argv[1:]
    main(path=input_file, path=output_file)
