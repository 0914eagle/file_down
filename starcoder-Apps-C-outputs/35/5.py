
import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

a = sorted(a)
a.insert(0, 0)
a.append(n+1)

res = 0

for i in range(m+1):
    res += min(a[i+1]-a[i]-1, 1)

print(res)
