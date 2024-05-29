
import math

def restore_array(n, gcd_table):
    a = [0] * n
    for i in range(n):
        a[i] = max(gcd_table)  # Choose the maximum value in the table as a divisor
        for j in range(n):
            if a[i] != gcd_table[j]:  # Update the table by dividing the other numbers by the chosen divisor
                gcd_table[j] = math.gcd(a[i], gcd_table[j])
    
    return a

# Input
n = int(input())
gcd_table = list(map(int, input().split()))

# Restore array
result = restore_array(n, gcd_table)

# Output
print(*result)
```
