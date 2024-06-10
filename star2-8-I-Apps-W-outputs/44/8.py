
def solve(perm, pairs):
    positions = {num: i for i, num in enumerate(perm)}
    for a, b in pairs:
        positions[perm[a-1]], positions[perm[b-1]] = positions[perm[b-1]], positions[perm[a-1]]
        perm[a-1], perm[b-1] = perm[b-1], perm[a-1]
    return perm

n, m = map(int, input().split())
perm = list(map(int, input().split()))
pairs = [list(map(int, input().split())) for _ in range(m)]
print(*solve(perm, pairs))

