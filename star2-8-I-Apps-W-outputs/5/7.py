
from itertools import product
from collections import defaultdict


def find_way(n, m, k, maze, initial_pos):
    directions = [
        (0, -1, "L"),
        (0, 1, "R"),
        (-1, 0, "U"),
        (1, 0, "D"),
    ]
    graph = defaultdict(list)
    for row in range(n):
        for col in range(m):
            if maze[row][col] == "*":
                continue
            for dx, dy, direction in directions:
                new_row = row + dx
                new_col = col + dy
                if 0 <= new_row < n and 0 <= new_col < m and maze[new_row][new_col] != "*":
                    graph[(row, col)].append((new_row, new_col, direction))
    for length in range(1, k + 1):
        for path in product(graph[initial_pos], repeat=length):
            current_pos = initial_pos
            for _, next_pos, direction in path:
                current_pos = next_pos
            if current_pos == initial_pos:
                return "".join(direction for _, _, direction in path)
    return "IMPOSSIBLE"


n, m, k = map(int, input().split())
maze = [list(input()) for _ in range(n)]
initial_pos = None
for row in range(n):
    for col in range(m):
        if maze[row][col] == "X":
            initial_pos = (row, col)
            break
    if initial_pos is not None:
        break
print(find_way(n, m, k, maze, initial_pos))

