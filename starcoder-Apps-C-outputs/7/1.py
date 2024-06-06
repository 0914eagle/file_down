
import math
n = int(input())

ans = 0
for i in range(n):
    x,y,r = map(float,input().split())
    l = (x**2 + y**2)**0.5
    ans += max(0, math.floor(l/r))
print(ans)
