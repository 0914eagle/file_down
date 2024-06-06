

n = int(input())
x = []
y = []
for i in range(n):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)
x.append(x[0])
y.append(y[0])

dx = [0] * (n+1)
dy = [0] * (n+1)

for i in range(n):
    dx[i] = x[i+1] - x[i]
    dy[i] = y[i+1] - y[i]

sx = [0] * (n+1)
sy = [0] * (n+1)
for i in range(n):
    sx[i+1] = sx[i] + dx[i]
    sy[i+1] = sy[i] + dy[i]

ans = 0
for i in range(n):
    ans += abs(dx[i] * sx[i] - x[i] * sx[n] + sy[n] * y[i] - sy[i] * y[n])
ans *= 2
ans /= n * (n+1) * (n+2)

print(ans)

