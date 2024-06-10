
n, k = map(int, input().split())
rs = list(map(int, input().split()))
quarrels = set()
for _ in range(k):
    x, y = map(int, input().split())
    quarrels.add((x, y))
    quarrels.add((y, x))
res = [0] * n
for i in range(n):
    for j in range(n):
        if rs[i] > rs[j] and (i+1, j+1) not in quarrels:
            res[i] += 1
print(' '.join(map(str, res)))

