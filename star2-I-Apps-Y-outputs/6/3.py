
def solve(n, x, y):
    x = sorted(x)
    y = sorted(y)
    path = ''
    for i in range(n):
        path += 'R' * x[i]
        path += 'U' * y[i]
    return path


t = int(input())
for _ in range(t):
    n = int(input())
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    path = solve(n, x, y)
    if path:
        print('YES')
        print(path)
    else:
        print('NO')

