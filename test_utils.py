import numpy as np
import pytest

from utils import (
    create_map_from_file,
    create_visited_matrix,
    get_matrix_size_from_file,
    get_neighbours,
    split_by_chars,
)


@pytest.mark.parametrize(
    "content, size",
    [
        ("001", (1, 3)),
        ("0\n1\n0", (3, 1)),
        ("10\n01", (2, 2)),
        ("00\n11\n00", (3, 2)),
    ],
)
def test_get_matrix_size(file, content, size):
    curr_file = file(content)
    assert get_matrix_size_from_file(curr_file) == size


@pytest.mark.parametrize(
    "string, result",
    [
        ("001", ["0", "0", "1"]),
        ("0\n1\n0", ["0", "\n", "1", "\n", "0"]),
    ],
)
def test_split_by_chars(string, result):
    assert split_by_chars(string) == result


@pytest.mark.parametrize(
    "content, y, x",
    [
        ("001", 1, 3),
        ("0\n1\n0", 3, 1),
        ("10\n01", 2, 2),
        ("00\n11\n00", 3, 2),
    ],
)
def test_create_map(file, content, y, x):
    curr_file = file(content)
    arr = create_map_from_file(curr_file, x, y)
    expected_arr = [
        [int(char) for char in split_by_chars(string)] for string in content.split()
    ]
    expected_arr = np.array(expected_arr, dtype=np.bool_)
    assert (arr == expected_arr).all()


@pytest.mark.parametrize(
    "y, x",
    [
        (1, 3),
        (3, 1),
        (2, 2),
        (3, 2),
    ],
)
def test_create_visited_matrix(y, x):
    arr = create_visited_matrix(x, y)
    expected_arr = np.zeros((y, x), dtype=np.bool_)
    assert (arr == expected_arr).all()


@pytest.mark.parametrize(
    "cords, y, x, result",
    [
        ((0, 0), 5, 5, [(0, 1), (1, 0), (1, 1)]),
        (
            (1, 1),
            5,
            5,
            [(0, 0), (0, 1), (1, 0), (0, 2), (2, 0), (2, 1), (0, 2), (1, 2), (2, 2)],
        ),
        ((1, 2), 3, 3, [(0, 2), (0, 1), (1, 1), (2, 1), (2, 2)]),
    ],
)
def test_get_neighbours(cords, y, x, result):
    # I use set here because the above result may have
    # different order of items because I put them by hand.
    assert set(get_neighbours(cords, x, y)) == set(result)
