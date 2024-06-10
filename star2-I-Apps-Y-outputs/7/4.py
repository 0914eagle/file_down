
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
        if x == 0:
            res.append(cnt)
        else:
            res.append(-1)
    return res

print(*solve(a, b), sep="\n")

