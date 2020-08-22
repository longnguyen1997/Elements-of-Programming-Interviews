from test_framework import generic_test
from math import pow

def ss_decode_col_id(col: str) -> int:
    bases = {c: i + 1 for i, c in enumerate(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    )}
    col_id = 0
    for i, c in enumerate(col):
        col_id += bases[c] * pow(26, len(col) - i - 1)
    return col_id


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
