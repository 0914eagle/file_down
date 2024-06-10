
from bisect import bisect_left
n, k = map(int, input().split())
r = list(map(int, input().split()))
pairs = [tuple(map(int, input().split())) for _ in range(k)]
quarrel = set(pairs)
can_be_mentor = [0] * n
for i, skill in enumerate(r):
    can_be_mentor[i] = bisect_left(r, skill + 1)
    for x, y in pairs:
        if x == i + 1:
            can_be_mentor[i] -= 1
        elif y == i + 1:
            can_be_mentor[i] -= 1
print(' '.join(map(str, can_be_mentor)))

