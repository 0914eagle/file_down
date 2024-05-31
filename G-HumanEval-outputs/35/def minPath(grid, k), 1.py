
def minPath(grid, k):
    def get_neighbors(i, j):
        neighbors = []
        if i > 0:
            neighbors.append((i - 1, j))
        if i < len(grid) - 1:
            neighbors.append((i + 1, j))
        if j > 0:
            neighbors.append((i, j - 1))
        if j < len(grid[0]) - 1:
            neighbors.append((i, j + 1))
        return neighbors

    def dfs(path, i, j):
        if len(path) == k:
            return path

        neighbors = get_neighbors(i, j)
        next_neighbor = None
        for ni, nj in neighbors:
            if grid[ni][nj] not in path:
                if next_neighbor is None or grid[ni][nj] < next_neighbor:
                    next_neighbor = grid[ni][nj]
                    next_i, next_j = ni, nj

        path.append(next_neighbor)
        return dfs(path, next_i, next_j)

    start_values = [grid[i][j] for i in range(len(grid)) for j in range(len(grid[0])]
    start_values.sort()
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == start_values[0]:
                return dfs([grid[i][j]], i, j)

# Test Cases
print(minPath([[1,2,3], [4,5,6], [7,8,9]], 3))  # Output: [1, 2, 1]
print(minPath([[5,9,3], [4,1,6], [7,8,2]], 1))  # Output: [1]
```
