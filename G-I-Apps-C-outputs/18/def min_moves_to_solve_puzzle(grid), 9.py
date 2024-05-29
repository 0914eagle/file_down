
def min_moves_to_solve_puzzle(grid):
    target = ['R', 'G', 'B', 'Y']
    moves = 0
    for i in range(4):
        row = grid[i]
        moves += min(row.index(target[i]), 4 - row.index(target[i]))
    return moves

# Read input
grid = [list(input()) for _ in range(4)]

# Call the function and output the result
print(min_moves_to_solve_puzzle(grid))
```
