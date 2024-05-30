
def get_diagonal_letters(grid):
    diagonal_letters = ""
    for i in range(3):
        diagonal_letters += grid[i][i]
    return diagonal_letters

# Input
grid = []
for _ in range(3):
    row = input().strip()
    grid.append(row)

# Output
print(get_diagonal_letters(grid))
```
