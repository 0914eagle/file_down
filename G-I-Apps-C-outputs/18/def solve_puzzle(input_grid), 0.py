
def solve_puzzle(input_grid):
    goal_grid = ['RRRR', 'GGGG', 'BBBB', 'YYYY']
    
    def grid_to_string(grid):
        return ''.join(row for row in grid)
    
    def manhattan_distance(grid1, grid2):
        total_distance = 0
        for i in range(4):
            for j in range(4):
                index1 = grid1[i][j]
                index2 = grid2[i][j]
                x1, y1 = divmod(index1, 4)
                x2, y2 = divmod(index2, 4)
                total_distance += abs(x1 - x2) + abs(y1 - y2)
        return total_distance

    current_grid = [list(row) for row in input_grid]
    
    min_moves = float('inf')
    for _ in range(4):
        for _ in range(4):
            min_moves = min(min_moves, manhattan_distance(current_grid, goal_grid))
            current_grid = [list(col) for col in zip(*current_grid)]
        current_grid = current_grid[-1:] + current_grid[:-1]

    return min_moves

input_grid = [
    "RGGR",
    "GBGB",
    "BYBY",
    "YRYR"
]
print(solve_puzzle(input_grid))
```
