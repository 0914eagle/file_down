
def solve(n, packages):
    packages.sort(key=lambda p: (p[0], p[1]))
    x, y = 0, 0
    path = ''
    for i in range(n):
        dx = packages[i][0] - x
        dy = packages[i][1] - y
        path += 'R' * dx
        path += 'U' * dy
        x, y = packages[i][0], packages[i][1]
    return path


t = int(input())
for _ in range(t):
    n = int(input())
    packages = []
    for _ in range(n):
        x, y = map(int, input().split())
        packages.append((x, y))
    path = solve(n, packages)
    if path:
        print('YES')
        print(path)
    else:
        print('NO')

