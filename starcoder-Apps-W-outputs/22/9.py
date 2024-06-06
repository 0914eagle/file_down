
import sys
from collections import Counter
n = 1000000
a = sys.stdin.readline().rstrip()
l = len(a)
p = a.find('^')

weight = [0 for _ in range(n)]
for i in range(l):
    if a[i].isdigit():
        weight[i] = int(a[i])
    else:
        weight[i] = 0

left = 0
right = 0
for i in range(p):
    left += weight[i] * (p - i)

for i in range(p + 1, l):
    right += weight[i] * (i - p)

if left == right:
    print('balance')
elif left > right:
    print('left')
else:
    print('right')
