
import math

def restore_array(n, gcd_table):
    a = [0] * n
    for i in range(n):
        for j in range(n):
            if i != j:
                gcd_val = gcd_table[i * n + j]
                a[i] = max(a[i], gcd_val)
    return a

# Reading input
n = int(input())
gcd_table = list(map(int, input().split()))

# Restoring the array
result = restore_array(n, gcd_table)

# Printing the result
print(*result)
