
n, q = map(int, input().split())
a = list(map(int, input().split()))
b = [int(input()) for _ in range(q)]

def solve(a, b):
    a.sort()
    res = []
    for x in b:
        cnt = 0
        while x > 0:
            idx = bisect.bisect_left(a, x)
            if idx < len(a):
                x -= a[idx]
                cnt += 1
            else:
                break
        if x > 0:
            res.append(-1)
        else:
            res.append(cnt)
    return res

res = solve(a, b)
for x in res:
    print(x)

