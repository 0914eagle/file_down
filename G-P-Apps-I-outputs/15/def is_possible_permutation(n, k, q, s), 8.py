
def is_possible_permutation(n, k, q, s):
    def apply_permutation(p, perm):
        return [p[idx-1] for idx in perm]

    def inverse_permutation(perm):
        inv_perm = [0] * len(perm)
        for i in range(len(perm)):
            inv_perm[perm[i]-1] = i + 1
        return inv_perm

    p = list(range(1, n+1))
    for _ in range(k):
        choice = random.choice(['heads', 'tails'])
        if choice == 'heads':
            p = apply_permutation(p, q)
        else:
            p = apply_permutation(p, inverse_permutation(q))

    if p == s:
        return "YES"
    else:
        return "NO"

# Input processing
n, k = map(int, input().split())
q = list(map(int, input().split()))
s = list(map(int, input().split()))

print(is_possible_permutation(n, k, q, s))
```
