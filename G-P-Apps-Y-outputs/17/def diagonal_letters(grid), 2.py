
def diagonal_letters(grid):
    return ''.join(grid[i][i] for i in range(3))

# Input processing
grid = [input().strip() for _ in range(3)]

# Output
print(diagonal_letters(grid))
```
