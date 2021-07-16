import sys
from queue import PriorityQueue

import numpy as np

from utils import create_map, create_visited_matrix, get_matrix_size, get_neighbours


# BFS based method
def count_islands(x: int, y: int, world_map: np.memmap, visited: np.memmap) -> int:
    islands_no = 0
    walking_on_island = False

    q = PriorityQueue()
    q.put((-int(world_map[0][0]), (0, 0)))

    while not q.empty():
        field, cords = q.get()

        i, j = cords

        # Because elem might have been added to the queue multiple times
        if visited[i][j]:
            continue

        visited[i][j] = True

        # -1 because I negated the number before I put it on the queue
        # and it's cheaper to negate this than access elem in an array.
        if field == -1 and not walking_on_island:
            islands_no += 1
            walking_on_island = True
        elif field != -1 and walking_on_island:
            walking_on_island = False

        for neighbour in get_neighbours(cords, x, y):
            i, j = neighbour
            if not visited[i][j]:
                q.put((-int(world_map[i][j]), (i, j)))

    return islands_no


if __name__ == "__main__":
    if len(sys.argv) < 2 or not sys.argv[1] or not sys.argv[1].endswith(".txt"):
        print("You should provide a correct file name as a input to the program!")
        sys.exit(0)

    file_name = sys.argv[1]
    y, x = get_matrix_size(file_name)
    world_map = create_map(file_name, x, y)
    visited = create_visited_matrix(x, y)
    islands_no = count_islands(x, y, world_map, visited)

    print(islands_no)
