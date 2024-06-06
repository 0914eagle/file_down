
import sys
sys.stdin=open('in.txt', 'r')
sys.stdout=open('out.txt', 'w')

import math
r, x1, y1, x2, y2 = map(int, input().split())
d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
if d <= r:
    print(x1, y1, r)
else:
    print(x1, y1, d)
