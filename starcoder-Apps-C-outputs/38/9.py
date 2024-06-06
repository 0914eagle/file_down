
#code
import math
n, k = map(int, input().split())
ans = 0
for i in range(1, n+1):
  ans += int(i**k)
print(ans%1000000007)
