
def diagonal_letters(grid):
    letters = [grid[i][i] for i in range(3)]
    return ''.join(letters)

# Input handling
grid = [input() for _ in range(3)]
print(diagonal_letters(grid))
```
