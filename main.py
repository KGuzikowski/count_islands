from utils import create_map, create_visited_matrix, get_matrix_size

if __name__ == "__main__":
    x, y = get_matrix_size("map.txt")
    world_map = create_map("map.txt", x, y)
    visited = create_visited_matrix(x, y)

    # BFS based method
