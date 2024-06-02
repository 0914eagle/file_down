
def find_connected_component_size(n, m, field):
    def dfs(x, y, component_size):
        if x < 0 or x >= n or y < 0 or y >= m or visited[x][y] or field[x][y] == '*':
            return
        visited[x][y] = True
        component_size[0] += 1
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            dfs(x + dx, y + dy, component_size)

    result = []
    visited = [[False for _ in range(m)] for _ in range(n)]

    for i in range(n):
        row = ""
        for j in range(m):
            if field[i][j] == '.':
                row += "."
            else:
                component_size = [0]
                dfs(i, j, component_size)
                row += str(component_size[0] % 10)
        result.append(row)

    return result

# Input
n, m = map(int, input().split())
field = [input() for _ in range(n)]

# Output
result = find_connected_component_size(n, m, field)
for row in result:
    print(row)
