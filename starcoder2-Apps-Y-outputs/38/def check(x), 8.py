
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

def check(x):
    cnt = 1
    l = 0
    r = 0
    while r < n:
        if a[r] - a[l] <= x:
            r += 1
        else:
            l = r
            cnt += 1
    return cnt <= k

l = 0
r = 10**9
while l < r:
    m = (l + r) // 2
    if check(m):
        r = m
    else:
        l = m + 1
print(n - l)

