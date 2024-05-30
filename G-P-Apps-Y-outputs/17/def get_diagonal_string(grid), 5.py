
def get_diagonal_string(grid):
    diagonal = ""
    for i in range(len(grid)):
        diagonal += grid[i][i]
    return diagonal

# Input
grid = []
for _ in range(3):
    row = input()
    grid.append(row)

# Output
print(get_diagonal_string(grid))
```
