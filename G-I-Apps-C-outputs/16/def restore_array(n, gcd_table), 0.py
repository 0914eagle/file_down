
import math

def restore_array(n, gcd_table):
    a = []
    
    for i in range(n):
        if i == 0:
            a.append(int(math.sqrt(max(gcd_table))))
        else:
            found = False
            for j in range(len(a)):
                if gcd_table[i*n + j] == 1:
                    a.append(a[j])
                    found = True
                    break
            if not found:
                current_gcd = gcd_table[i*n]
                for k in range(1, len(a)):
                    current_gcd = math.gcd(current_gcd, gcd_table[i*n + k])
                a.append(current_gcd)
    
    return a

# Taking input
n = int(input())
gcd_table = list(map(int, input().split()))

# Restoring the array
array_a = restore_array(n, gcd_table)

# Printing the result
print(*array_a)
```
