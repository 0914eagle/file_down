
def min_moves_to_solve_puzzle(grid):
    target = 'RGBY' * 4
    start = ''.join(grid)
    
    def moves_to_target(s):
        return min(s.count(target[i:] + target[:i]) for i in range(4))

    return min(moves_to_target(start[i:] + start[:i]) for i in range(4))

# Read input
grid = [input() for _ in range(4)]

# Calculate and output minimum number of moves
print(min_moves_to_solve_puzzle(grid))
```
