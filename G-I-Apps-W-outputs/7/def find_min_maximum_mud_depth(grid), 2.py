
def find_min_maximum_mud_depth(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    max_depth = 0
    
    for r in range(rows):
        min_depth = min(grid[r])
        max_depth = max(max_depth, min_depth)
        
    return max_depth

# Read input
r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(r)]

# Call the function and print the result
print(find_min_maximum_mud_depth(grid))
```
