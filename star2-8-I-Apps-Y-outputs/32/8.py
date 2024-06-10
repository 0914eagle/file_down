
n, k = map(int, input().split())
r = list(map(int, input().split()))
pairs = [tuple(map(int, input().split())) for _ in range(k)]
quarrel = [False] * (n + 1)
for x, y in pairs:
    quarrel[x] = quarrel[y] = True
mentors = [0] * (n + 1)
for i in range(1, n + 1):
    if not quarrel[i]:
        for j in range(1, n + 1):
            if r[i - 1] > r[j - 1] and not quarrel[j]:
                mentors[i] += 1
for x in mentors[1:]:
    print(x, end=" ")

