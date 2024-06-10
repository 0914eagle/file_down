
n, k = list(map(int, input().split()))
r = list(map(int, input().split()))
q = set()
for i in range(k):
    x, y = list(map(int, input().split()))
    q.add((x, y))

cnt = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if r[i - 1] > r[j - 1] and (i, j) not in q and (j, i) not in q:
            cnt[i] += 1
            cnt[j] += 1

print(*cnt)

