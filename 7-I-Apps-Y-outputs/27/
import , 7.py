
import sys

N, K = map(int, sys.stdin.readline().split())

d = []
for i in range(K):
    d.append(int(sys.stdin.readline()))

a = []
for i in range(K):
    a.append(list(map(int, sys.stdin.readline().split())))

ans = 0
for i in range(N):
    if i+1 not in a[i][0]:
        ans += 1

print(ans)

