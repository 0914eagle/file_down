
def solve_peace_lightning(n):
    if n == 2:
        return 3, [2, 1, 2]
    
    bombs = [2]
    for i in range(3, n + 1):
        bombs.append(i)
    for i in range(1, n):
        bombs.append(n - i)
    
    return len(bombs), bombs

n = int(input())
m, bombs = solve_peace_lightning(n)
print(m)
print(' '.join(map(str, bombs)))
