
def diagonal_string(grid):
    diagonal = ''
    for i in range(3):
        diagonal += grid[i][i]
    return diagonal

grid = [input() for _ in range(3)]
print(diagonal_string(grid))
```
