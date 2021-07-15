import numpy as np
from tempfile import mkdtemp
import os.path as path
from typing import Tuple


# Unfortunately, because the file might be too big for memory
# I need to count lines to set a proper shape for memmap.
def get_matrix_size(file_path: str) -> Tuple[int, int]:
    with open(file_path, "r") as file:
        x = y = 0

        for line in file:
            if x == 0:
                x = len(line.strip())
            y += 1

    return x, y


def create_map(file_path: str, x: int, y: int) -> Tuple[np.memmap, int, int]:
    with open(file_path, "r") as file:
        name = path.join(mkdtemp(), 'temp_arr.dat')
        arr = np.memmap(name, dtype=np.bool_, mode='w+', shape=(y, x))

        for i, line in enumerate(file):
            for j, field in enumerate(line.strip()):
                arr[i][j] = int(field)

    return arr


def create_visited_matrix(y: int, x: int) -> np.memmap:
    name = path.join(mkdtemp(), 'visited_arr.dat')
    return np.memmap(name, dtype=np.bool_, mode='w+', shape=(y, x))
