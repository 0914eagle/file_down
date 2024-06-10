
n, m, h = map(int, input().split())
u = list(map(int, input().split()))
c = [list(map(int, input().split())) for _ in range(m)]

def check(x):
    for i in range(m):
        if u[x-1] == u[c[i][0]-1] or u[x-1] == u[c[i][1]-1]:
            return False
    return True

ans = []
for i in range(1, n+1):
    if check(i):
        ans.append(i)

print(len(ans))
print(*ans)

