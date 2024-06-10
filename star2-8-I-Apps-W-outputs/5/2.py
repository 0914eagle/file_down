
def find_path(x, y, k, path, grid, n, m):
    if k == 0:
        return path
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x = x + dx
        new_y = y + dy
        if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] != '*' and (new_x, new_y) not in path:
            new_path = find_path(new_x, new_y, k - 1, path + [(new_x, new_y)], grid, n, m)
            if new_path:
                return new_path


n, m, k = map(int, input().split())
grid = [list(input()) for _ in range(n)]

x, y = 0, 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'X':
            x, y = i, j

path = find_path(x, y, k, [(x, y)], grid, n, m)

if not path:
    print("IMPOSSIBLE")
else:
    moves = ""
    for i in range(1, len(path)):
        x1, y1 = path[i - 1]
        x2, y2 = path[i]
        if x2 == x1 + 1:
            moves += "D"
        elif x2 == x1 - 1:
            moves += "U"
        elif y2 == y1 + 1:
            moves += "R"
        else:
            moves += "L"

    print(moves)


