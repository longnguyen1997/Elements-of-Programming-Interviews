from typing import List

from test_framework import generic_test


def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    def traverse_and_flood(x, y, original_color):
        if not 0 <= x < len(image) or not 0 <= y < len(image[0]):
            return
        if image[x][y] is not original_color:
            return
        image[x][y] = not original_color
        traverse_and_flood(x - 1, y, original_color)
        traverse_and_flood(x, y + 1, original_color)
        traverse_and_flood(x + 1, y, original_color)
        traverse_and_flood(x, y - 1, original_color)
    traverse_and_flood(x, y, image[x][y])


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
