
def min_mud_depth(r, c, grid):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    max_mud_depth = float('-inf')
    
    for i in range(r):
        visited = [[False] * c for _ in range(r)]
        stack = [(i, 0)]
        
        while stack:
            row, col = stack.pop()
            visited[row][col] = True
            max_mud_depth = max(max_mud_depth, grid[row][col])
            
            if col == c - 1:
                break
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                if 0 <= new_row < r and 0 <= new_col < c and not visited[new_row][new_col]:
                    stack.append((new_row, new_col))
    
    return max_mud_depth

# Reading inputs
r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(r)]

# Calling the function and printing output
print(min_mud_depth(r, c, grid))
```
