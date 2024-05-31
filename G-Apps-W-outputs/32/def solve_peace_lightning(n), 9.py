
def solve_peace_lightning(n):
    if n == 2:
        return 3, [2, 1, 2]
    
    bombs = [2] + list(range(1, n+1)) + [2]
    return len(bombs), bombs

# Input
n = 3

# Solve and print output
min_bombs, bomb_positions = solve_peace_lightning(n)
print(min_bombs)
print(" ".join(map(str, bomb_positions)))
