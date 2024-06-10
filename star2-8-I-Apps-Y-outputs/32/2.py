
n, k = map(int, input().split())
r = list(map(int, input().split()))
quarrels = set()
for i in range(k):
    x, y = map(int, input().split())
    if x > y:
        x, y = y, x
    quarrels.add((x, y))

mentors = [0] * n
for i in range(n):
    for j in range(n):
        if r[i] > r[j] and (i+1, j+1) not in quarrels:
            mentors[i] += 1

print(*mentors)

