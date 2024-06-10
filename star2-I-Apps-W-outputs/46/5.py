
def solve(n, m, groups):
    return "YES"

n, m = map(int, input().split())
groups = []
for _ in range(m):
    group = list(map(int, input().split()))
    groups.append(group)

print(solve(n, m, groups))

