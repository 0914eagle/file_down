
from itertools import permutations

def solve(n, packages):
    if n == 0:
        return ""
    if n == 1:
        return "R" * packages[0][0] + "U" * packages[0][1]
    
    min_path = "R" * packages[0][0] + "U" * packages[0][1]
    for perm in permutations(packages[1:]):
        path = "R" * perm[0][0] + "U" * perm[0][1]
        for i in range(1, n):
            path += "R" * (perm[i][0] - perm[i - 1][0]) + "U" * (perm[i][1] - perm[i - 1][1])
        
        if len(path) < len(min_path) or (len(path) == len(min_path) and path < min_path):
            min_path = path
    
    return min_path

t = int(input())
for _ in range(t):
    n = int(input())
    packages = []
    for _ in range(n):
        x, y = map(int, input().split())
        packages.append((x, y))
    
    packages.sort(key=lambda p: p[0] + p[1])
    
    path = solve(n, packages)
    
    if path:
        print("YES")
        print(path)
    else:
        print("NO")

