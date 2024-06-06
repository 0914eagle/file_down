
#usr/bin/python3

import math

R, x1, y1, x2, y2 = map(float, input().split())

if (abs(x1) - R) <= abs(x2) <= (abs(x1) + R) and abs(y1) <= abs(y2) <= (abs(y1) + R):
    print(x1, y1, abs(x1 - x2) - R)
else:
    a = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    b = (a + R) / 2
    x = x2 + (x1 - x2) * b / a
    y = y2 + (y1 - y2) * b / a
    r = math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
    print(x, y, r)
