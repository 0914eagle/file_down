
n, m = [int(x) for x in input().split()]
p = [int(x) for x in input().split()]
for _ in range(m):
    a, b = [int(x) for x in input().split()]
    p[a-1], p[b-1] = p[b-1], p[a-1]
print(' '.join(map(str, p)))

