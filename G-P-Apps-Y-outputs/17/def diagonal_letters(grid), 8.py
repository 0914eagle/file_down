
def diagonal_letters(grid):
    letters = [grid[i][i] for i in range(3)]
    return ''.join(letters)

grid = [input().strip() for _ in range(3)]
result = diagonal_letters(grid)
print(result)
```
