
n, m = list(map(int, input().split()))
perm = list(map(int, input().split()))
pos = [0]*(n+1)
for i in range(n):
    pos[perm[i]] = i
for _ in range(m):
    a, b = list(map(int, input().split()))
    pos[perm[a-1]], pos[perm[b-1]] = pos[perm[b-1]], pos[perm[a-1]]
    perm[a-1], perm[b-1] = perm[b-1], perm[a-1]

max_pos = n
for i in range(n-1, -1, -1):
    if pos[i] < max_pos:
        perm[pos[i]] = i
        max_pos = pos[i]

print(*perm)

