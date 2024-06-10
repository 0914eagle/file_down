
n, m = map(int, input().split())
x, y, t = [], [], []
for _ in range(n):
    xi, yi, ti = map(int, input().split())
    x.append(xi)
    y.append(yi)
    t.append(ti)

def dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

res = 0
for i in range(m):
    d = [dist(0, 0, x[i], y[i]) for i in range(n) if t[i] == i+1]
    res += min(d)
print(res)

