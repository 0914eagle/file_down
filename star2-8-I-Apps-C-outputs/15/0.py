
n = int(input())
a = list(map(int, input().split()))
min_val = min(a)
if min_val == 0:
    print(-1)
else:
    res = 0
    for i in range(n):
        if a[i] % min_val != 0:
            res += a[i] % min_val
    print(res)

