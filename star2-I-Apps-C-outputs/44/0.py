
def solve(n, m, h, u, c):
    pass

n, m, h = map(int, input().split())
u = list(map(int, input().split()))
c = [list(map(int, input().split())) for _ in range(m)]

print(*solve(n, m, h, u, c))

