
def check_permutation(n, k, q, s):
    def apply_permutation(p, perm):
        return [p[i-1] for i in perm]
    
    p = list(range(1, n+1))
    
    for _ in range(k):
        if p == s:
            return "YES"
        coin = True  # Assume heads
        if coin:
            p = apply_permutation(p, q)
        else:
            p = apply_permutation(p, [q.index(i)+1 for i in range(1, n+1)])
    return "NO"

# Read input
n, k = map(int, input().split())
q = list(map(int, input().split()))
s = list(map(int, input().split()))

# Check permutation possibility
result = check_permutation(n, k, q, s)
print(result)
```
