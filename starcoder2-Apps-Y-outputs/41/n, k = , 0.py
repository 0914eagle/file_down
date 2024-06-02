
n, k = map(int, input().split())
a = list(map(int, input().split()))

l, r = 1, 10**9
while l < r:
    m = (l + r) // 2
    cnt = 0
    for i in range(n):
        if a[i] <= m:
            cnt += 1
    if cnt >= k:
        r = m
    else:
        l = m + 1
if l == 10**9 and k != 0:
    print(-1)
else:
    print(l)

