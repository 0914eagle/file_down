
def solve(n, q, painters):
    pass

n, q = map(int, input().split())
painters = []
for _ in range(q):
    l, r = map(int, input().split())
    painters.append((l, r))
print(solve(n, q, painters))

