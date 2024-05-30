
def diagonal_letters(grid):
    letters = []
    for i in range(3):
        letters.append(grid[i][i])
    return ''.join(letters)

grid = [input() for _ in range(3)]
result = diagonal_letters(grid)
print(result)
```
