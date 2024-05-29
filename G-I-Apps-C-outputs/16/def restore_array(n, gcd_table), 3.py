
import math

def restore_array(n, gcd_table):
    a = [0] * n
    for i in range(n):
        a[i] = gcd_table[i*n] // gcd_table[i*n+1]
    
    return a

# Input parsing
n = int(input())
gcd_table = list(map(int, input().split()))

# Restore array and output result
result = restore_array(n, gcd_table)
print(*result)
```
