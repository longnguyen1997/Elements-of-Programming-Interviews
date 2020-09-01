from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    delimiter, current, previous = '/', '.', '..'
    pathnames = []  # Stack.
    for name in path.split(delimiter):
        if name == previous:
            if not pathnames or pathnames[-1] == previous:
                pathnames.append(name)
            else:
                pathnames.pop()
        # Skip empties and current folders.
        elif name and name != current:
            pathnames.append(name)
    joined_path = delimiter.join(pathnames)
    # Account for absolute paths.
    if path[0] == delimiter:
        return delimiter + joined_path
    # Else, relative.
    return joined_path


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
