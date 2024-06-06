
n, m = map(int, input().split())
def binarySearch():
    left = 0
    right = n
    mid = (left + right) // 2
    while left < right:
        if n - mid <= 1:
            return mid
        if f(mid) == 0:
            right = mid
        else:
            left = mid + 1
        mid = (left + right) // 2
    return mid

def f(mid):
    i = 0
    for x in xlist:
        if x >= mid:
            break
        i += 1
    if i % 2 == 1:
        return -1
    else:
        return 1

xlist = []
for _ in range(m):
    x1, x2, y = map(int, input().split())
    xlist.append(x1)
    xlist.append(x2)
xlist = sorted(xlist)
xlist.append(n)

if m == 0:
    print("0" * n)
else:
    ans = ""
    mid = binarySearch()
    if mid == 0:
        ans += "0" * n
    else:
        ans += "+" * (mid - 1)
        ans += "0" * (n - mid)
    print(ans)
