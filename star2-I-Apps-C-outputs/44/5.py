
n, m, h = map(int, input().split())
u = list(map(int, input().split()))
c = [list(map(int, input().split())) for _ in range(m)]

def check(k, x):
    for i in range(m):
        if u[x[i]-1] == u[c[i][0]-1] or u[x[i]-1] == u[c[i][1]-1]:
            return False
    return True

def solve():
    for k in range(1, n+1):
        for x in combinations(range(1, n+1), k):
            if check(k, x):
                return k, x

k, x = solve()
print(k)
print(*x)

