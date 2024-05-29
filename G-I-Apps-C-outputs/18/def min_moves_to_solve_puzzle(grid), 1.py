
def min_moves_to_solve_puzzle(grid):
    target = ["RRRR", "GGGG", "BBBB", "YYYY"]
    current = [row for row in grid]
    
    def find_row(row_num, color):
        for i, row in enumerate(current):
            if row.count(color) == 4 and row != target[row_num]:
                return i
        return -1
    
    def move_row_left(row_num, times):
        current[row_num] = current[row_num][times:] + current[row_num][:times]
    
    moves = 0
    for i in range(4):
        color = target[i][0]
        row = find_row(i, color)
        if row != i:
            diff = (row - i) % 4
            if diff <= 2:
                move_row_left(row, diff)
            else:
                move_row_left(row, 4 - diff)
            moves += 1
    
    return moves

# Read input
grid = [input().strip() for _ in range(4)]

# Calculate and print minimum number of moves needed to solve the puzzle
print(min_moves_to_solve_puzzle(grid))
```
