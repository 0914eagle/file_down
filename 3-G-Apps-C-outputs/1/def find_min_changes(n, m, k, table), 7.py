
def find_min_changes(n, m, k, table):
    def dfs(i, j, val):
        if i < 0 or i >= n or j < 0 or j >= m or visited[i][j] or table[i][j] != val:
            return
        visited[i][j] = True
        components[-1].append((i, j))
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            dfs(i + dx, j + dy, val)

    def is_rectangle(component):
        min_row = min(row for row, _ in component)
        max_row = max(row for row, _ in component)
        min_col = min(col for _, col in component)
        max_col = max(col for _, col in component)
        return len(component) == (max_row - min_row + 1) * (max_col - min_col + 1)

    def count_changes(component):
        min_row = min(row for row, _ in component)
        max_row = max(row for row, _ in component)
        min_col = min(col for _, col in component)
        max_col = max(col for _, col in component)
        return min(len(component) - (max_row - min_row + 1) * (max_col - min_col + 1), len(component))

    visited = [[False for _ in range(m)] for _ in range(n)]
    components = []
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                components.append([])
                dfs(i, j, table[i][j])

    changes = 0
    for component in components:
        if not is_rectangle(component):
            return -1
        changes += count_changes(component)

    return changes if changes <= k else -1

# Input parsing
n, m, k = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

result = find_min_changes(n, m, k, table)
print(result)
