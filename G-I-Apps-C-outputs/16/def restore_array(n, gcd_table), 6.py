
import math

def restore_array(n, gcd_table):
    a = [0] * n
    a[0] = int(math.sqrt(gcd_table[0]))
    
    for i in range(1, n):
        a[i] = gcd_table[i] // a[0]
    
    return a

# Input
n = int(input())
gcd_table = list(map(int, input().split()))

# Restore the array
result = restore_array(n, gcd_table)

# Output
print(*result)
```
