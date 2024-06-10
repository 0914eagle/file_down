
m1, m2, m3 = map(int, input().split())
x1, x2, x3 = map(int, input().split())
y1, y2, y3 = map(int, input().split())

def find_distance(m, x, y):
    for d in range(y + 1):
        if (x + d) % m == 0 or (x - d) % m == 0:
            return d
    return None

d1 = find_distance(m1, x1, y1)
d2 = find_distance(m2, x2, y2)
d3 = find_distance(m3, x3, y3)

if d1 is None or d2 is None or d3 is None:
    print('No solution')
else:
    z = d1 * m2 * m3 + d2 * m1 * m3 + d3 * m1 * m2
    print(z)

