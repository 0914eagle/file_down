
import sys

n, m, c = map(int, sys.stdin.readline().split())
b = list(map(int, sys.stdin.readline().split()))

a = []
for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

ans = 0
for i in range(n):
    flag = True
    for j in range(m):
        if a[i][j] * b[j] + c <= 0:
            flag = False
            break
    if flag:
        ans += 1

print(ans)

