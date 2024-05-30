
def diagonal_letters(grid):
    return ''.join([grid[i][i] for i in range(3)])

grid = [input() for _ in range(3)]
result = diagonal_letters(grid)
print(result)
```
