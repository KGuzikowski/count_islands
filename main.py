from queue import PriorityQueue

from utils import create_map, create_visited_matrix, get_matrix_size, get_neighbours

if __name__ == "__main__":
    x, y = get_matrix_size("map.txt")
    world_map = create_map("map.txt", x, y)
    visited = create_visited_matrix(x, y)
    islands_no = 0
    walking_on_island = False

    # BFS based method
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

    print(islands_no)
