
def solve(n):
    bombs = [n]
    for i in range(n-1, 0, -1):
        bombs.append(i)
    return len(bombs), bombs

n = int(input())
m, bombs = solve(n)
print(m)
print(" ".join(map(str, bombs)))
