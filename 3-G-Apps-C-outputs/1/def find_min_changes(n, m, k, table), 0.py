
def find_min_changes(n, m, k, table):
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
        return len(component) == (max_row - min_row + 1) * (max_col - min_col + 1)
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    changes = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                components = [[]]
                dfs(i, j, table[i][j])
                for component in components:
                    if not check_rectangle(component):
                        return -1
                    if len(component) % 2 == 1:
                        changes += 1
    return changes if changes <= k else -1

# Input parsing
n, m, k = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

result = find_min_changes(n, m, k, table)
print(result)
