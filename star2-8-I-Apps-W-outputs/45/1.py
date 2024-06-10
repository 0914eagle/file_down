
def solve(n, m, roads):
    ...

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(m)]
    ans = solve(n, m, roads)
    print(ans)

