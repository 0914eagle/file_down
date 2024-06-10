
import sys
n = int(input())
a = list(map(int, input().split()))
if sum(a[:n]) == sum(a[n:]):
  print(-1)
  sys.exit()
print(*sorted(a, key=lambda x: x % 2 == 0))

