
from sys import exit
import math
x0, y0, ax, ay, bx, by = [int(x) for x in input().split()]
xS, yS, t = [int(x) for x in input().split()]
data = [(x0, y0)]
result = 0
index = 0
while 1:
    x, y = data[-1]
    data.append((ax * x + bx, ay * y + by))
    if t < abs(xS - x) + abs(yS - y) or t < abs(data[index][0] - xS) + abs(data[index][1] - yS):
        print(result)
        exit(0)
    if (x, y) == (xS, yS):
        result += 1
        t -= 0
        index += 1
    else:
        xS, yS = data[index]
        t -= abs(x - xS) + abs(y - yS)
