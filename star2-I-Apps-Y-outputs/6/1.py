
def solve(n, packages):
    packages = sorted(packages, key=lambda x: (x[0], x[1]))
    x, y = 0, 0
    path = ""
    for i in range(n):
        dx = packages[i][0] - x
        dy = packages[i][1] - y
        if dx < 0 or dy < 0:
            return "NO"
        path += "R" * dx + "U" * dy
        x, y = packages[i][0], packages[i][1]
    return path

t = int(input())
for _ in range(t):
    n = int(input())
    packages = [list(map(int, input().split())) for _ in range(n)]
    path = solve(n, packages)
    print("YES" if path != "NO" else "NO")
    print(path)

