
def min_moves_to_equal_strings(s, t):
    n = len(s)
    m = len(t)
    
    if s == t:
        return 0
    
    for i in range(min(n, m)):
        if s[i] != t[i]:
            return n + m - 2*i
    
    return abs(n - m)

# Input
s = input().strip()
t = input().strip()

# Output
print(min_moves_to_equal_strings(s, t))
```
