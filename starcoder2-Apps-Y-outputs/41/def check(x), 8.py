
n, k = map(int, input().split())
a = list(map(int, input().split()))

def check(x):
    cnt = 0
    for i in a:
        if i <= x:
            cnt += 1
    return cnt >= k

l, r = 1, 10**9
while l < r:
    m = (l + r) // 2
    if check(m):
        r = m
    else:
        l = m + 1

if check(l):
    print(l)
else:
    print(-1)

