
def find_connected_component_size(n, m, field):
    def dfs(x, y, component_id):
        if x < 0 or x >= n or y < 0 or y >= m or visited[x][y] or field[x][y] == '*':
            return
        visited[x][y] = True
        component_sizes[component_id] += 1
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dfs(x + dx, y + dy, component_id)

    visited = [[False for _ in range(m)] for _ in range(n)]
    component_sizes = {}
    component_id = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and field[i][j] == '.':
                component_sizes[component_id] = 0
                dfs(i, j, component_id)
                component_id += 1

    result = [['.' for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if field[i][j] == '*':
                connected_component_size = 0
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == '.':
                        connected_component_size += component_sizes[nx * m + ny]
                result[i][j] = str(connected_component_size % 10)

    return result

n, m = map(int, input().split())
field = [list(input().strip()) for _ in range(n)]

output = find_connected_component_size(n, m, field)
for row in output:
    print(''.join(row))
