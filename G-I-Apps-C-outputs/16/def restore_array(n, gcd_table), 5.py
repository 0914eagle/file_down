
import math

def restore_array(n, gcd_table):
    a = [0] * n
    
    first_row = gcd_table[:n]
    a[0] = max(first_row)
    
    for i in range(1, n):
        a[i] = gcd_table[i*n]
    
    return a

# Input
n = int(input())
gcd_table = list(map(int, input().split()))

# Output
result = restore_array(n, gcd_table)
print(*result)
```
