
def destroy_tanks(n):
    bombs = []
    for i in range(n, 1, -1):
        bombs.append(i)
    for i in range(1, n+1):
        bombs.append(i)
    return len(bombs), bombs

# Input
n = 3
# Output
m, bomb_positions = destroy_tanks(n)
print(m)
print(' '.join(map(str, bomb_positions)))
