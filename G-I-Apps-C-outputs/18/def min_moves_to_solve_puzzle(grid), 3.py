
def min_moves_to_solve_puzzle(grid):
    def moves_to_solve_row(row):
        colors = ['R', 'G', 'B', 'Y']
        min_moves = float('inf')
        for i in range(4):
            moves = 0
            for j in range(4):
                moves += min(abs(colors.index(row[j]) - colors.index(colors[(i+j)%4])), abs(colors.index(row[j]) - colors.index(colors[(i-j)%4]))
            min_moves = min(min_moves, moves)
        return min_moves
    
    total_moves = 0
    for row in grid:
        total_moves += moves_to_solve_row(row)
    
    return total_moves

# Input parsing
input_grid = []
for _ in range(4):
    input_grid.append(input())

# Call the function with the input
result = min_moves_to_solve_puzzle(input_grid)
print(result)
```
