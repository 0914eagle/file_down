
def solve_tomb_puzzle(n, m, floorplan):
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m

    def is_mirror(char):
        return char == '\\' or char == '/'

    def rotate_gargoyle(gargoyle):
        return 'V' if gargoyle == 'H' else 'H'

    def get_neighbors(x, y):
        neighbors = []
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            while is_valid(nx, ny) and floorplan[nx][ny] != '#' and not gargoyles_visited[nx][ny]:
                neighbors.append((nx, ny))
                if is_mirror(floorplan[nx][ny]):
                    break
                nx += dx
                ny += dy
        return neighbors

    def dfs(x, y):
        if floorplan[x][y] == '#':
            return
        gargoyles_visited[x][y] = True
        if floorplan[x][y] == 'V' or floorplan[x][y] == 'H':
            gargoyle_count[rotate_gargoyle(floorplan[x][y])] += 1
        
        for nx, ny in get_neighbors(x, y):
            dfs(nx, ny)

    gargoyle_count = {'V': 0, 'H': 0}
    gargoyles_visited = [[False for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if not gargoyles_visited[i][j]:
                dfs(i, j)

    if gargoyle_count['V'] != gargoyle_count['H']:
        return -1
    return gargoyle_count['V']

# Read input
n, m = map(int, input().split())
floorplan = [input() for _ in range(n)]

# Solve the tomb puzzle
result = solve_tomb_puzzle(n, m, floorplan)
print(result)
```
