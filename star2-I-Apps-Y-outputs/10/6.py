
a, b = map(int, input().split())
m, sigma = map(int, input().split())

def R(x, y):
    return a*x + b*y

def outlets(x, y):
    return 2*x + y

def constraints(x, y):
    return x >= 1 and y >= 1 and x + y <= m and outlets(x, y) >= sigma

def solve(x, y):
    if constraints(x, y):
        return R(x, y)
    elif x == 1 and y == 1:
        return 0
    elif x == 1:
        return solve(x, y-1)
    elif y == 1:
        return solve(x-1, y)
    else:
        return max(solve(x-1, y), solve(x, y-1))

print(solve(m, m))

