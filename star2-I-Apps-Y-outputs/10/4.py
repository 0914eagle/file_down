
a, b = map(int, input().split())
m, sigma = map(int, input().split())

def R(x, y):
    return a*x + b*y

def is_valid(x, y):
    if x < 1 or y < 1:
        return False
    if x + y > m:
        return False
    if 2*x + y < sigma:
        return False
    return True

def find_max_R():
    max_R = -1
    max_x = -1
    max_y = -1
    for x in range(1, m+1):
        for y in range(1, m+1):
            if is_valid(x, y):
                r = R(x, y)
                if r > max_R:
                    max_R = r
                    max_x = x
                    max_y = y
    return max_R, max_x, max_y

max_R, max_x, max_y = find_max_R()
print(max_R)

