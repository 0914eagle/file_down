
# https://codeforces.com/contest/1225/submission/77994339
def f(d):
    if not d:
        return
    if len(d) == 1:
        return d
    if len(d) == 2:
        return [d]
    d.sort()
    r = []
    for i in range(len(d) - 1):
        r.append([d[i], d[i + 1]])
    r = f(r)
    if not r:
        return
    return [d] + r

n = int(input())
d = []
for _ in range(n):
    a = list(map(int, input().split()))
    d += a[1:]
d = list(set(d))

d = f(d)
if not d:
    print("impossible")
else:
    r = []
    for x in d:
        for i in range(len(x) - 1):
            r.append([x[i], x[i + 1]])
    for x in r:
        print(" ".join(map(str, x)))
