
def change_table(n, m, k, table):
    def dfs(i, j, val):
        if i < 0 or i >= n or j < 0 or j >= m or visited[i][j] or table[i][j] != val:
            return
        visited[i][j] = True
        components[-1].append((i, j))
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            dfs(i + dx, j + dy, val)

    def get_component_size(component):
        min_row, min_col = float('inf'), float('inf')
        max_row, max_col = 0, 0
        for row, col in component:
            min_row = min(min_row, row)
            min_col = min(min_col, col)
            max_row = max(max_row, row)
            max_col = max(max_col, col)
        return (max_row - min_row + 1) * (max_col - min_col + 1)

    def change_cells(component):
        size = get_component_size(component)
        return size if size % 2 == 0 else size + 1

    visited = [[False for _ in range(m)] for _ in range(n)]
    components = []

    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                components.append([])
                dfs(i, j, table[i][j])

    changes = 0
    for component in components:
        size = get_component_size(component)
        if size % 2 == 1:
            changes += change_cells(component) if k > 0 else -1
            k -= 1

    return changes

# Input
n, m, k = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

# Output
result = change_table(n, m, k, table)
print(result if result >= 0 else -1)
