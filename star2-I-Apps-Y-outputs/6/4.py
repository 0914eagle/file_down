
from itertools import permutations

def solve(n, packages):
    if n == 0:
        return ""
    if n == 1:
        return "R" * packages[0][0] + "U" * packages[0][1]
    best_path = None
    best_cost = float("inf")
    for perm in permutations(range(n)):
        path = ""
        cost = 0
        x, y = 0, 0
        for i in perm:
            dx, dy = packages[i][0] - x, packages[i][1] - y
            cost += dx + dy
            path += "R" * dx + "U" * dy
            x, y = packages[i][0], packages[i][1]
        if cost < best_cost or (cost == best_cost and path < best_path):
            best_cost = cost
            best_path = path
    return best_path

t = int(input())
for _ in range(t):
    n = int(input())
    packages = [tuple(map(int, input().split())) for _ in range(n)]
    path = solve(n, packages)
    if path is None:
        print("NO")
    else:
        print("YES")
        print(path)

