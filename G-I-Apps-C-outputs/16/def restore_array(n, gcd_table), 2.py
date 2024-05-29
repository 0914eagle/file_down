
from math import gcd

def restore_array(n, gcd_table):
    gcd_table.sort(reverse=True)
    a = [gcd_table[0]]
    for i in range(1, n):
        a.append(gcd_table[i] // a[0])
    
    return a

# Read input
n = int(input())
gcd_table = list(map(int, input().split()))

# Restore array a
a = restore_array(n, gcd_table)

# Output the array elements
print(' '.join(map(str, a)))
```
