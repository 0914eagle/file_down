
import sys

n, k = map(int, input().split())

d = [0] * k
for i in range(k):
    d[i] = int(input())

a = [[] for i in range(k)]
for i in range(k):
    a[i] = list(map(int, input().split()))

ans = 0
for i in range(n):
    if sum(a[j].count(i + 1) for j in range(k)) == 0:
        ans += 1

print(ans)

