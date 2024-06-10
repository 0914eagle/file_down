
n = int(input())
c = list(map(int, input().split()))
s = set(c)
if len(s) < n:
    print("IMPOSSIBLE")
else:
    l = 0
    r = 0
    res = []
    for i in range(n):
        if c[i] not in s:
            continue
        l = i + 1
        while i < n and c[i] == c[l - 1]:
            i += 1
        r = i
        res.append([l, r, c[l - 1]])
    print(len(res))
    for item in res:
        print(item[0], item[1], item[2])

