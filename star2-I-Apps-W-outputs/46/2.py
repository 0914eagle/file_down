
def solve(n, m, groups):
    return "YES"

n, m = map(int, input().split())
groups = []
for _ in range(m):
    k, *group = map(int, input().split())
    groups.append(group)

print(solve(n, m, groups))

