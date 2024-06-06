
# https://www.luogu.com.cn/problem/P5758

n, m = list(map(int, input().split()))
p = list(map(int, input().split()))
r = list(map(int, input().split()))
c = []
t = []
for i in range(n):
    c.append(list(map(int, input().split()))[0])
    t.append(list(map(int, input().split()))[0])

t.sort()
c.sort()
ans = 0
x = 0
y = 0
clo = set()
for i in range(n):
    if t[i] >= x:
        while t[i] >= x:
            if not clo:
                clo.add(c[i])
                x += p[c[i] - 1]
            else:
                break
        while t[i] >= y:
            if clo:
                clo.remove(c[i])
                y += r[c[i] - 1]
            else:
                break
        if not clo:
            ans += 1
print(ans)
