
n, k = map(int, input().split())
a = list(map(int, input().split()))
u = set()
for x in a:
    u.add(x)
if len(u) < k:
    print('NO')
else:
    print('YES')
    b = list(u)
    c = [0] * n
    for i in range(n):
        c[i] = b[i % k] + 1
    print(*c)

