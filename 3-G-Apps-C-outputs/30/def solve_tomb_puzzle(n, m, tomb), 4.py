
def solve_tomb_puzzle(n, m, tomb):
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m

    def get_neighbors(x, y):
        neighbors = []
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                neighbors.append((new_x, new_y))
        return neighbors

    def dfs(x, y, visited):
        visited.add((x, y))
        for nx, ny in get_neighbors(x, y):
            if (nx, ny) not in visited and tomb[nx][ny] != '#':
                dfs(nx, ny, visited)

    def count_components():
        visited = set()
        components = 0
        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and tomb[i][j] != '#':
                    dfs(i, j, visited)
                    components += 1
        return components

    components = count_components()
    if components != 1:
        return -1

    rotations = 0
    for i in range(n):
        for j in range(m):
            if tomb[i][j] in ['V', 'H']:
                neighbors = get_neighbors(i, j)
                has_neighbor = False
                for nx, ny in neighbors:
                    if tomb[nx][ny] in ['V', 'H']:
                        has_neighbor = True
                        break
                if not has_neighbor:
                    rotations += 1

    return rotations

# Input
n, m = map(int, input().split())
tomb = [input() for _ in range(n)]

# Output
print(solve_tomb_puzzle(n, m, tomb))
