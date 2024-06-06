
N, M = map(int, input().split())

res = 0
for i in range(N):
    s = input()
    cur = 0
    for j in range(M):
        if s[j] == 'A':
            cur += 5
        elif s[j] == 'B':
            cur += 4
        elif s[j] == 'C':
            cur += 3
        elif s[j] == 'D':
            cur += 2
        elif s[j] == 'E':
            cur += 1
    res = max(res, cur)

a = list(map(int, input().split()))

for i in range(M):
    res += a[i]

print(res)
