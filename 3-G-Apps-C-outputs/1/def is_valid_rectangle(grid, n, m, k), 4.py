
def is_valid_rectangle(grid, n, m, k):
    def dfs(i, j, value):
        if i < 0 or i >= n or j < 0 or j >= m or visited[i][j] or grid[i][j] != value:
            return
        visited[i][j] = True
        components[-1].append((i, j))
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dfs(i + dx, j + dy, value)

    def is_rectangle(component):
        min_row, max_row = min(cell[0] for cell in component), max(cell[0] for cell in component)
        min_col, max_col = min(cell[1] for cell in component), max(cell[1] for cell in component)
        return len(component) == (max_row - min_row + 1) * (max_col - min_col + 1)

    def count_changes(component):
        min_row, max_row = min(cell[0] for cell in component), max(cell[0] for cell in component)
        min_col, max_col = min(cell[1] for cell in component), max(cell[1] for cell in component)
        return min(len(component), (max_row - min_row + 1) * (max_col - min_col + 1))

    visited = [[False for _ in range(m)] for _ in range(n)]
    components = []
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                components.append([])
                dfs(i, j, grid[i][j])

    changes_required = 0
    for component in components:
        if not is_rectangle(component):
            return -1
        changes_required += count_changes(component)

    return changes_required if changes_required <= k else -1

# Input
n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Output
result = is_valid_rectangle(grid, n, m, k)
print(result)
