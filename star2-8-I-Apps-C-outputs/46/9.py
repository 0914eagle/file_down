
m1, m2, m3 = map(int, input().split())
x1, x2, x3 = map(int, input().split())
y1, y2, y3 = map(int, input().split())
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
def lcm(a, b):
    return a * b // gcd(a, b)
l = lcm(m1, lcm(m2, m3))
def calc_interval(x, y, m):
    interval = []
    for i in range(-y, y + 1):
        interval.append((x + i) % m)
    return interval
interval1 = calc_interval(x1, y1, m1)
interval2 = calc_interval(x2, y2, m2)
interval3 = calc_interval(x3, y3, m3)
res = []
for x1 in interval1:
    for x2 in interval2:
        for x3 in interval3:
            if (x1 * m2 * m3 + x2 * m1 * m3 + x3 * m1 * m2) % l == 0:
                res.append(x1 * m2 * m3 + x2 * m1 * m3 + x3 * m1 * m2)
print(min(res))

