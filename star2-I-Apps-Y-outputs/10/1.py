
a, b = map(int, input().split())
m, sigma = map(int, input().split())

def rent(x, y):
    return a*x + b*y

def outlet(x, y):
    return 2*x + y

def constraint1(x, y):
    return x >= 1 and y >= 1

def constraint2(x, y):
    return x + y <= m

def constraint3(x, y):
    return outlet(x, y) >= sigma

def solve(x, y):
    if constraint1(x, y) and constraint2(x, y) and constraint3(x, y):
        return rent(x, y)
    else:
        return -1

def search(x, y):
    if x > m or y > m:
        return -1
    else:
        return max(solve(x, y), search(x+1, y), search(x, y+1))

print(search(1, 1))

