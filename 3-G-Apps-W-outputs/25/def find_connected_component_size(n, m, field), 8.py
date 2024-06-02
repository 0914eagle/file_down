
def find_connected_component_size(n, m, field):
    def dfs(x, y, component_id):
        if x < 0 or x >= n or y < 0 or y >= m or visited[x][y] or field[x][y] == '*':
            return 0
        visited[x][y] = True
        size = 1
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            size += dfs(x + dx, y + dy, component_id)
        return size

    result = []
    visited = [[False for _ in range(m)] for _ in range(n)]
    component_id = 1

    for i in range(n):
        row = ""
        for j in range(m):
            if field[i][j] == '*':
                size = dfs(i, j, component_id) % 10
                row += str(size)
                component_id += 1
            else:
                row += '.'
        result.append(row)

    return result

# Input
n, m = map(int, input().split())
field = [input() for _ in range(n)]

# Output
result = find_connected_component_size(n, m, field)
for row in result:
    print(row)
