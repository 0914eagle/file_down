
def is_possible(n, k, q, s):
    def apply_permutation(p, q):
        return [p[q[i] - 1] for i in range(n)]
        
    def can_reach_target(p, s, k):
        if k == 0:
            return p == s
        
        if can_reach_target(apply_permutation(p, q), s, k - 1):
            return True
        if can_reach_target([q.index(i) + 1 for i in p], s, k - 1):
            return True
        
        return False
    
    initial_permutation = list(range(1, n+1))
    
    if can_reach_target(initial_permutation, s, k):
        return "YES"
    else:
        return "NO"

# Input reading
n, k = map(int, input().split())
q = list(map(int, input().split()))
s = list(map(int, input().split()))

# Output
print(is_possible(n, k, q, s))
```
