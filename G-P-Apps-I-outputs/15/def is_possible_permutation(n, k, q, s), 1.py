
def is_possible_permutation(n, k, q, s):
    p = list(range(1, n+1))
    
    for _ in range(k):
        p = [p[q[i]-1] for i in range(n)]
        if p == s:
            return "YES"
    
    return "NO"

# Input parsing
n, k = map(int, input().split())
q = list(map(int, input().split()))
s = list(map(int, input().split()))

# Check if the situation is possible
result = is_possible_permutation(n, k, q, s)
print(result)
```
