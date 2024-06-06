
import math
R, x1, y1, x2, y2 = map(int, input().split())
r = math.sqrt(x2**2 + y2**2)
if r > R:
    print(x1, y1, r)
else:
    if r <= 0.5*R:
        print(x1, y1, R)
    else:
        d = R - r
        x, y = x1 + d*x2/r, y1 + d*y2/r
        print(x, y, R)
