
def find_min_depth(r, c, grid):
    def is_valid(x, y, visited):
        return 0 <= x < r and 0 <= y < c and not visited[x][y]
    
    def dfs(x, y, visited, depth):
        visited[x][y] = True
        max_depth = depth
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y, visited):
                new_depth = max_depth
                if grid[new_x][new_y] > max_depth:
                    new_depth = grid[new_x][new_y]
                max_depth = max(max_depth, dfs(new_x, new_y, visited, new_depth))
        return max_depth

    min_depth = float('inf')
    for i in range(r):
        visited = [[False for _ in range(c)] for _ in range(r)]
        min_depth = min(min_depth, dfs(i, 0, visited, grid[i][0]))
    
    return min_depth

# Read input
r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(r)]

# Call the function and print the output
print(find_min_depth(r, c, grid))
```
