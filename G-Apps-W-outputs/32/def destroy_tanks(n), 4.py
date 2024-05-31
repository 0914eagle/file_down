
def destroy_tanks(n):
    bombs = [1] * n
    bombs[0] = n
    return n + 1, bombs

# Input
n = 3

# Output
m, bombs = destroy_tanks(n)
print(m)
print(' '.join(map(str, bombs)))
