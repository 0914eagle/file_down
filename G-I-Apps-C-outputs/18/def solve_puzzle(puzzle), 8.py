
def solve_puzzle(puzzle):
    target = ['R', 'G', 'B', 'Y']
    moves = 0
    
    def calculate_moves(row):
        nonlocal moves
        for color in target:
            if color in row:
                moves += abs(row.index(color) - target.index(color))
    
    for i in range(4):
        calculate_moves(puzzle[i])
    
    return moves

# Read the input
input_lines = []
for _ in range(4):
    input_lines.append(input())

# Solve the puzzle
result = solve_puzzle(input_lines)

# Output the result
print(result)
```
