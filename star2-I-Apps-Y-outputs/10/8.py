
a, b = map(int, input().split())
m, sigma = map(int, input().split())

def rent(x, y):
    return a*x + b*y

def outlets(x, y):
    return 2*x + y

def is_valid(x, y):
    return x >= 1 and y >= 1 and x + y <= m and outlets(x, y) >= sigma

x = 1
y = m - x

while not is_valid(x, y):
    x += 1
    y = m - x

print(rent(x, y))

