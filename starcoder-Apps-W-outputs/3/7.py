
n, k, q = map(int, input().split())

a = [0 for i in range(200002)]

for _ in range(n):
    l, r = map(int, input().split())
    a[l] += 1
    a[r+1] -= 1

for i in range(200001):
    a[i+1] += a[i]

b = []
for i in range(200002):
    if a[i] >= k:
        b.append(i)

for _ in range(q):
    l, r = map(int, input().split())
    l = bisect.bisect_left(b, l)
    r = bisect.bisect_right(b, r)
    print(r-l)

