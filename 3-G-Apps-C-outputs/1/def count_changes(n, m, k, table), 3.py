
def count_changes(n, m, k, table):
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
    
    def count_changes_helper(component):
        min_row, max_row = min(cell[0] for cell in component), max(cell[0] for cell in component)
        min_col, max_col = min(cell[1] for cell in component), max(cell[1] for cell in component)
        return max((max_row - min_row + 1) * (max_col - min_col + 1) - len(component), 0)
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    components = []
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                components.append([])
                dfs(i, j, table[i][j])
    
    changes_needed = 0
    for component in components:
        if not check_rectangle(component):
            return -1
        changes_needed += count_changes_helper(component)
    
    return changes_needed if changes_needed <= k else -1

# Input parsing
n, m, k = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

result = count_changes(n, m, k, table)
print(result)
