
import sys
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = 0
tmp = 0
for i in range(n):
    tmp += a[i]
    if tmp > b[i]:
        print("Impossible")
        sys.exit(0)
    if tmp == b[i]:
        res += 1
        tmp = 0
print(res, sum(a))
