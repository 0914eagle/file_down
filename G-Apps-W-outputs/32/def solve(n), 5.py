
def solve(n):
    if n == 2:
        return 3, [2, 1, 2]
    
    bombs = [2]
    for i in range(2, n):
        bombs.append(i)
    bombs.append(2)
    
    return n+1, bombs

# Input
n = int(input())

# Output
m, bomb_positions = solve(n)
print(m)
print(" ".join(map(str, bomb_positions)))
