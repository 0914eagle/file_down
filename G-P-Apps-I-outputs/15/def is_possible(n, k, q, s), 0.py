
def is_possible(n, k, q, s):
    def apply_permutation(perm, q):
        return [perm[q[i] - 1] for i in range(len(perm))]
    
    p = [i for i in range(1, n+1)]
    
    for _ in range(k):
        t = apply_permutation(p, q)
        if t == s:
            return "YES"
        p = apply_permutation(t, q)
    
    return "NO"

# Input
n, k = map(int, input().split())
q = list(map(int, input().split()))
s = list(map(int, input().split()))

# Output
print(is_possible(n, k, q, s))
```
