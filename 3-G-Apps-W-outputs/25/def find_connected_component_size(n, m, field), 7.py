
def find_connected_component_size(n, m, field):
    def dfs(x, y, component_id):
        if x < 0 or x >= n or y < 0 or y >= m or visited[x][y] or field[x][y] == '*':
            return
        visited[x][y] = True
        component_sizes[component_id] += 1
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            dfs(x + dx, y + dy, component_id)
    
    component_sizes = {}
    component_id = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and field[i][j] == '.':
                component_sizes[component_id] = 0
                dfs(i, j, component_id)
                component_id += 1
    
    output = []
    for i in range(n):
        row = ''
        for j in range(m):
            if field[i][j] == '.':
                row += '.'
            else:
                component_id = 0
                for k in range(len(component_sizes)):
                    if visited[i][j]:
                        component_id = k
                        break
                row += str(component_sizes[component_id] % 10)
        output.append(row)
    
    return output

# Input
n, m = map(int, input().split())
field = [input() for _ in range(n)]

# Output
result = find_connected_component_size(n, m, field)
for row in result:
    print(row)
