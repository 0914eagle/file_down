
n, m = map(int, input().split())
a = list(map(int, input().split()))
l = [0] * m
r = [0] * m
for i in range(m):
    l[i], r[i] = map(int, input().split())

def calc(a, l, r):
    b = a[:]
    for i in range(len(l)):
        for j in range(l[i] - 1, r[i]):
            b[j] -= 1
    return max(b) - min(b)

d = 0
q = 0
c = []
for i in range(1, 1 << m):
    tmp = []
    for j in range(m):
        if (i >> j) & 1:
            tmp.append(j + 1)
    if calc(a, [l[x - 1] for x in tmp], [r[x - 1] for x in tmp]) > d:
        d = calc(a, [l[x - 1] for x in tmp], [r[x - 1] for x in tmp])
        q = len(tmp)
        c = tmp

print(d)
print(q)
print(*c)

