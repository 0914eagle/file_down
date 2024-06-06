
# 网友题解
n, m = map(int, input().split())
p, s = [], []
for i in range(n):
    a, b, c, d, *f = map(int, input().split())
    s.append(str(f))
    p.append([b*30+d, a*30+c])
# check if every event has the same duration
for i in range(m):
    tmp = []
    for j in range(n):
        tmp.append(p[j][1]-p[j][0]-sum([int(s[j][k][i]) for k in range(n)]))
    if tmp[1:] != tmp[:-1]:
        print(-1)
        break
else:
    res = []
    for i in range(m):
        res.append(tmp[0]//(n-1)+sum([int(s[j][i]) for j in range(n)]))
    print(*res)
