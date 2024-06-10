
import math

def solve(x):
    x = x % 360
    if x == 0:
        return 0
    if x > 0:
        return math.ceil(x / 90)
    return 4 - math.ceil(-x / 90)

x = int(input())
print(solve(x))

