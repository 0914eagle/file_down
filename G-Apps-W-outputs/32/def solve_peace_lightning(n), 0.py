
def solve_peace_lightning(n):
    if n == 2:
        return 3, [2, 1, 2]
    
    bombs = [2]
    for i in range(2, n + 1):
        bombs.append(i)
    bombs.extend(range(n, 1, -1))
    
    return 2*n, bombs

# Input
n = int(input())
m, bomb_positions = solve_peace_lightning(n)

# Output
print(m)
print(' '.join(map(str, bomb_positions)))
