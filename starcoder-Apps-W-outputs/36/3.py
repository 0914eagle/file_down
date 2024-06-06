

def is_circle(x, y, r, x1, y1, x2, y2):
    x1, y1, x2, y2 = x + x1, y + y1, x + x2, y + y2
    dis = (x1 - x) ** 2 + (y1 - y) ** 2
    if r ** 2 - dis <= 1e-6:
        return True
    dis = (x2 - x) ** 2 + (y2 - y) ** 2
    if r ** 2 - dis <= 1e-6:
        return True
    return False

n, m = map(int, input().split())

x, y, r = 0, 0, 1e9
for _ in range(n):
    x1, y1 = map(int, input().split())
    if is_circle(x, y, r, x1, y1, x1, y1):
        continue
    dx, dy = x - x1, y - y1
    r1 = ((dx ** 2 + dy ** 2) ** 0.5 + 1e-6) / 2
    dx, dy = (x1 - dx / 2, y1 - dy / 2)
    if r > r1:
        x, y, r = dx, dy, r1

for _ in range(m):
    x1, y1 = map(int, input().split())
    if is_circle(x, y, r, x1, y1, x1, y1):
        continue
    dx, dy = x - x1, y - y1
    r1 = ((dx ** 2 + dy ** 2) ** 0.5 + 1e-6) / 2
    dx, dy = (x1 - dx / 2, y1 - dy / 2)
    if r > r1:
        x, y, r = dx, dy, r1

if r > 10000:
    print('NO')
else:
    print('YES')
