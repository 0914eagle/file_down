
a, b = map(int, input().split())
m, sigma = map(int, input().split())
def R(x, y):
    return a*x + b*y
def x_min(y):
    return max(1, (sigma - y)/2)
def x_max(y):
    return min(m - y, 2*y)
def y_min(x):
    return max(1, m - x)
def y_max(x):
    return min(m - x, (sigma - 2*x)/2)
def R_max(x, y):
    return R(x, y)
x = y = 1
while x <= m:
    y = y_min(x)
    while y <= y_max(x):
        x = x_min(y)
        while x <= x_max(y):
            R_max = max(R_max, R(x, y))
            x += 1
        y += 1
    x += 1
print(R_max)

