
def check_permutation_possible(n, k, q, s):
    def apply_permutation(p, q):
        return [p[q[i] - 1] for i in range(len(p))]

    p = list(range(1, n + 1))
    
    for _ in range(k):
        t = apply_permutation(p, q)
        if t == s:
            return "YES"
        if t == p:
            return "NO"
        p = t

    return "NO"

# Input
n, k = map(int, input().split())
q = list(map(int, input().split()))
s = list(map(int, input().split()))

# Output
print(check_permutation_possible(n, k, q, s))
```
