
def is_permutation_possible(n, k, q, s):
    p = list(range(1, n+1))
    
    for i in range(k):
        new_p = [0] * n
        
        for j in range(n):
            if i % 2 == 0:
                new_p[q[j]-1] = p[j]
            else:
                new_p[j] = p[q[j]-1]
        
        p = new_p
    
    if p == s:
        return "YES"
    else:
        return "NO"

# Reading input
n, k = map(int, input().split())
q = list(map(int, input().split()))
s = list(map(int, input().split()))

# Checking if permutation is possible
result = is_permutation_possible(n, k, q, s)
print(result)
```
