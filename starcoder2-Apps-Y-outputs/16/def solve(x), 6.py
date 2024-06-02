
def solve(x):
    t = 0
    while x > 0:
        x -= t
        t += 1
    return t

x = int(input())
print(solve(x))

