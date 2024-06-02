
def is_valid_rectangle(table, n, m, k):
    def dfs(i, j, val):
        if i < 0 or i >= n or j < 0 or j >= m or visited[i][j] or table[i][j] != val:
            return
        visited[i][j] = True
        components[-1].append((i, j))
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            dfs(i + dx, j + dy, val)
    
    def is_rectangle(component):
        min_row, max_row = min(cell[0] for cell in component), max(cell[0] for cell in component)
        min_col, max_col = min(cell[1] for cell in component), max(cell[1] for cell in component)
        return len(component) == (max_row - min_row + 1) * (max_col - min_col + 1)
    
    def change_cells(component):
        min_row, max_row = min(cell[0] for cell in component), max(cell[0] for cell in component)
        min_col, max_col = min(cell[1] for cell in component), max(cell[1] for cell in component)
        for i in range(min_row, max_row + 1):
            for j in range(min_col, max_col + 1):
                if table[i][j] == 1:
                    table[i][j] = 0
                else:
                    table[i][j] = 1
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    changes = 0
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                components = [[]]
                dfs(i, j, table[i][j])
                if not is_rectangle(components[-1]):
                    return -1
                if len(components[-1]) % 2 != 0:
                    changes += 1
                    if changes > k:
                        return -1
                    change_cells(components[-1])
    
    return changes

n, m, k = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

result = is_valid_rectangle(table, n, m, k)
print(result)
