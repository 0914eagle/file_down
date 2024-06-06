
# Your code here!
from math import sqrt

n = int(input())

ans = 0
for i in range(n):
  x, y, r = map(float, input().split())
  d = sqrt(x*x+y*y)
  if d < r:
    ans += 1
  else:
    ans += 2
print(ans)
