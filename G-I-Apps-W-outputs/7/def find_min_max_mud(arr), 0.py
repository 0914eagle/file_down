
def find_min_max_mud(arr):
    rows = len(arr)
    cols = len(arr[0])
    
    # Initialize a 2D array to store the maximum depth of mud encountered up to that cell
    max_mud = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Fill the first column with the depths of mud
    for i in range(rows):
        max_mud[i][0] = arr[i][0]
        
    # Update the max_mud values for each cell based on the neighboring cells
    for j in range(1, cols):
        for i in range(rows):
            current_depth = arr[i][j]
            max_above = max_mud[i][j-1] if i > 0 else 0
            max_below = max_mud[i][j-1] if i < rows - 1 else 0
            max_mud[i][j] = max(current_depth, max_above, max_below)
    
    # Find the minimum value of the maximum depths of mud in the rightmost column
    min_max_mud = max_mud[0][-1]
    for i in range(1, rows):
        min_max_mud = min(min_max_mud, max_mud[i][-1])
    
    return min_max_mud

# Read input
r, c = map(int, input().split())
grid = []
for _ in range(r):
    row = list(map(int, input().split()))
    grid.append(row)

# Output the result
print(find_min_max_mud(grid))
```
