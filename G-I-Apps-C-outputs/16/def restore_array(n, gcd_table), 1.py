
import math

def restore_array(n, gcd_table):
    factors = set()
    for i in range(n):
        for j in range(n):
            if i != j:
                factors.add(gcd_table[i*n + j])
    
    a = [max(factors)]
    for i in range(1, n):
        a.append(gcd_table[i] // a[0])
    
    return a

# Input parsing
n = int(input().strip())
gcd_table = list(map(int, input().strip().split()))

# Restore array a
result = restore_array(n, gcd_table)

# Output the result
print(' '.join(map(str, result)))
```
