
def is_possible(n, k, q, s):
    def apply_permutation(p, perm):
        return [p[i - 1] for i in perm]

    p = list(range(1, n+1))
    
    for _ in range(k):
        coin_toss = random.choice(['heads', 'tails'])
        if coin_toss == 'heads':
            p = apply_permutation(p, q)
        else:
            p = apply_permutation(p, [q.index(i)+1 for i in p])

    return p == s

# Input parsing
n, k = map(int, input().split())
q = list(map(int, input().split()))
s = list(map(int, input().split()))

# Check if the situation is possible
if is_possible(n, k, q, s):
    print("YES")
else:
    print("NO")
```
