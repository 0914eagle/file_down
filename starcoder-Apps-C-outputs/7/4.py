
n = int(input())
e = []
for i in range(n):
    x, y, r = map(float, input().split())
    e.append((x, y, r))

def count(e, t):
    c = 0
    for x, y, r in e:
        a = y * t
        b = x * t
        d = x * x + y * y
        if d <= r * r and a * a + b * b < r * r:
            c += 1
    return c

lo = -1e10
hi = 1e10
while hi - lo > 1e-12:
    a = (lo * 2 + hi) / 3
    b = (lo + hi * 2) / 3
    if count(e, a) < count(e, b):
        lo = a
    else:
        hi = b
print(count(e, lo))
