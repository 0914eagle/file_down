
n, m = map(int, input().split())
p = list(map(int, input().split()))
q = {v: k for k, v in enumerate(p)}
for i in range(m):
    a, b = map(int, input().split())
    a, b = q[a], q[b]
    p[a], p[b] = p[b], p[a]
    q[p[a]], q[p[b]] = a, b
print(*p)

