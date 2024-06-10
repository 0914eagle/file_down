
from sys import stdin

def solve():
    n, m = map(int, stdin.readline().split())
    p = list(map(int, stdin.readline().split()))
    foe_pairs = [tuple(map(int, stdin.readline().split())) for _ in range(m)]
    foe_pairs_set = set(foe_pairs)
    ans = 0
    for i in range(n):
        for j in range(i, n):
            if any((p[i], p[j]) in foe_pairs_set or (p[j], p[i]) in foe_pairs_set for i in range(n) for j in range(i, n)):
                continue
            ans += 1
    
    print(ans)

solve()

