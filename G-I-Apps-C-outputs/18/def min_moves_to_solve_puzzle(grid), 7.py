
def min_moves_to_solve_puzzle(grid):
    target = ['R', 'G', 'B', 'Y']
    moves = 0
    
    for i in range(4):
        row = grid[i]
        target_row = target.index(row[0])
        move_row = min((target_row + j) % 4 for j in range(4))
        moves += move_row
        col = [grid[k][i] for k in range(4)]
        target_col = target.index(col[0])
        move_col = min((target_col + j) % 4 for j in range(4))
        moves += move_col
        
    return moves

# Read input from file
with open('input.txt', 'r') as file:
    grid = [list(line.strip()) for line in file]

# Call the function with input grid
result = min_moves_to_solve_puzzle(grid)
print(result)
```
