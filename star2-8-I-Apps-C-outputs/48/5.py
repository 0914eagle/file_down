
n = int(input())
c = list(map(int, input().split()))
l, r, col = 1, 1, c[0]
res = []
for i in range(n):
    if c[i] != col:
        res.append([l, r, col])
        l = i + 1
        col = c[i]
    r = i + 1
res.append([l, r, col])
if len(set(c)) == len(res):
    print(len(res))
    for l, r, col in res:
        print(l, r, col)
else:
    print("IMPOSSIBLE")

