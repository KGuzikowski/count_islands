import os.path as path
from itertools import product
from tempfile import mkdtemp
from typing import List, Tuple

import numpy as np


# Unfortunately, because the file might be too big for memory
# I need to count lines to set a proper shape for numpy's memmap.
def get_matrix_size(file_path: str) -> Tuple[int, int]:
    with open(file_path, "r") as file:
        x = y = 0

        for line in file:
            if x == 0:
                x = len(line.strip())
            y += 1

    return x, y


def create_map(file_path: str, x: int, y: int) -> np.memmap:
    with open(file_path, "r") as file:
        name = path.join(mkdtemp(), "temp_arr.dat")
        arr = np.memmap(name, dtype=np.bool_, mode="w+", shape=(y, x))

        for i, line in enumerate(file):
            for j, field in enumerate(line.strip()):
                arr[i][j] = int(field)

    return arr


def create_visited_matrix(x: int, y: int) -> np.memmap:
    name = path.join(mkdtemp(), "visited_arr.dat")
    return np.memmap(name, dtype=np.bool_, mode="w+", shape=(y, x))


def get_neighbours(cords: Tuple[int, int], x: int, y: int) -> List[Tuple[int, int]]:
    i, j = cords

    if i == 0:
        neigh_i = [i, i + 1]
    elif y - 1 > i > 0:
        neigh_i = [i - 1, i, i + 1]
    else:
        neigh_i = [i - 1, i]

    if j == 0:
        neigh_j = [j, j + 1]
    elif x - 1 > j > 0:
        neigh_j = [j - 1, j, j + 1]
    else:
        neigh_j = [j - 1, j]

    ret = list(product(neigh_i, neigh_j))
    ret.remove(cords)
    return ret
