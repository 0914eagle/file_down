
def change_table(n, m, k, table):
    def dfs(i, j, val):
        if i < 0 or i >= n or j < 0 or j >= m or visited[i][j] or table[i][j] != val:
            return
        visited[i][j] = True
        components[-1].append((i, j))
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            dfs(i + dx, j + dy, val)

    def check_rectangle(component):
        min_row, max_row = min(cell[0] for cell in component), max(cell[0] for cell in component)
        min_col, max_col = min(cell[1] for cell in component), max(cell[1] for cell in component)
        return (max_row - min_row + 1) * (max_col - min_col + 1) == len(component)

    def change_cells(component):
        min_row, max_row = min(cell[0] for cell in component), max(cell[0] for cell in component)
        min_col, max_col = min(cell[1] for cell in component), max(cell[1] for cell in component)
        return min(n * m - len(component), 2 * (max_row - min_row + 1) + 2 * (max_col - min_col + 1))

    visited = [[False for _ in range(m)] for _ in range(n)]
    components = []
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                components.append([])
                dfs(i, j, table[i][j])
    
    min_changes = float('inf')
    for component in components:
        if not check_rectangle(component):
            return -1
        min_changes = min(min_changes, change_cells(component))
    
    return min_changes if min_changes <= k else -1

# Input
n, m, k = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

# Output
result = change_table(n, m, k, table)
print(result)
