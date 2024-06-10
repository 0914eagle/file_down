
n, k = map(int, input().split())
r = list(map(int, input().split()))
mentors = [0] * n
quarrels = set()
for _ in range(k):
    x, y = map(int, input().split())
    quarrels.add((min(x, y), max(x, y)))
for i in range(n):
    for j in range(n):
        if i != j and r[i] > r[j] and (i + 1, j + 1) not in quarrels:
            mentors[i] += 1

print(*mentors)

