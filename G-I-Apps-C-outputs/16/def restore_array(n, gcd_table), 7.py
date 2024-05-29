
import math

def restore_array(n, gcd_table):
    a = [0] * n
    max_gcd = max(gcd_table)
    
    for i in range(n):
        candidate = gcd_table[i]
        possible_divisors = []
        for j in range(n):
            if i != j:
                possible_divisors.append(gcd_table[i*n+j] // candidate)
        divisor = max(set(possible_divisors), key = possible_divisors.count)
        a[i] = candidate // divisor
    
    return a

n = int(input())
gcd_table = list(map(int, input().split()))

result = restore_array(n, gcd_table)
print(' '.join(map(str, result)))
```
