
n = int(input())
p = []
for i in range(n):
    x,y = map(int, input().split())
    p.append((x,y))

p.append(p[0])

s = 0
for i in range(1,n+1):
    s += (p[i-1][0] - p[i][0]) * (p[i-1][1] + p[i][1])
s = abs(s) / 2

ans = 0
for i in range(n):
    a = p[i]
    b = p[i+1]
    ans += ((a[0]+b[0])*(a[1]-b[1])*(a[1]-b[1]))/6 + ((b[0]+a[0])*(b[1]-a[1])*(b[1]-a[1]))/6
ans = abs(ans)/s
print(ans)
