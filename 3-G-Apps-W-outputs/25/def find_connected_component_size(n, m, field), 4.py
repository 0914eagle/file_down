
def find_connected_component_size(n, m, field):
    def dfs(x, y, component_id):
        if x < 0 or x >= n or y < 0 or y >= m or visited[x][y] or field[x][y] == '*':
            return 0
        visited[x][y] = True
        size = 1
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            size += dfs(x + dx, y + dy, component_id)
        return size

    result = [['0' for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if field[i][j] == '*':
                visited = [[False for _ in range(m)] for _ in range(n)]
                component_size = dfs(i, j, 0) % 10
                result[i][j] = str(component_size)

    return result

n, m = map(int, input().split())
field = [list(input()) for _ in range(n)]

output = find_connected_component_size(n, m, field)
for row in output:
    print(''.join(row))
