
def min_moves_to_solve_puzzle(grid):
    target_grid = [
        ['R', 'R', 'R', 'R'],
        ['G', 'G', 'G', 'G'],
        ['B', 'B', 'B', 'B'],
        ['Y', 'Y', 'Y', 'Y']
    ]
    
    moves = 0
    for i in range(4):
        for j in range(4):
            if grid[i][j] != target_grid[i][j]:
                target_row = target_grid[i]
                target_col = [row[j] for row in target_grid]

                row_diff = min(abs(target_row.index(grid[i][j]) - j), abs(4 + target_row.index(grid[i][j]) - j))
                col_diff = min(abs(target_col.index(grid[i][j]) - i), abs(4 + target_col.index(grid[i][j]) - i))

                moves += row_diff + col_diff

    return moves

# Read the input
input_grid = []
for i in range(4):
    input_grid.append(list(input().strip()))
    
# Calculate and output the minimum number of moves needed to solve the puzzle
print(min_moves_to_solve_puzzle(input_grid))
```
