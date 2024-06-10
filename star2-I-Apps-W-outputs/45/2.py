
def solve(n, m, teleports):
    pass

n, m = map(int, input().split())
teleports = []
for _ in range(n):
    a, b = map(int, input().split())
    teleports.append((a, b))

print(solve(n, m, teleports))

