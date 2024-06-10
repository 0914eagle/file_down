
n, m, k = map(int, input().split())
maze = [input() for _ in range(n)]
start = None
for i in range(n):
    for j in range(m):
        if maze[i][j] == "X":
            start = (i, j)

def is_valid_cell(i, j):
    return 0 <= i < n and 0 <= j < m and maze[i][j] != "*"

def find_min_cycle(i, j, k, path):
    if k == 0:
        return path if i == start[0] and j == start[1] else None
    if k < 0:
        return None
    result = None
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = i + di, j + dj
        if not is_valid_cell(ni, nj):
            continue
        maze[ni][nj] = "*"
        new_path = find_min_cycle(ni, nj, k - 1, path + "U" if di == -1 else "D" if di == 1 else "L" if dj == -1 else "R")
        if new_path is not None and (result is None or result > new_path):
            result = new_path
        maze[ni][nj] = "."
    return result

result = find_min_cycle(start[0], start[1], k, "")
print(result if result is not None else "IMPOSSIBLE")

