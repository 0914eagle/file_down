
from math import ceil

b1, q, l, m = [int(x) for x in input().split()]
lst = [int(x) for x in input().split()]
cnt = 0
for i in range(1, l + 1):
    if i not in lst:
        cnt += 1
    elif abs(b1) <= i:
        break

if cnt == 0:
    print(0)
elif cnt == l:
    print("inf")
else:
    print(cnt)
