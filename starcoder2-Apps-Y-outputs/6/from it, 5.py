
from itertools import combinations

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    k -= 1
    s = ['a'] * (n - 2) + ['b'] * 2
    for i, j in combinations(range(n), 2):
        if k == 0:
            break
        if s[i] > s[j]:
            s[i], s[j] = s[j], s[i]
            k -= 1
    print(''.join(s))

