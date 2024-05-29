
import math

def calculate_gcd(a, b):
    if b == 0:
        return a
    return calculate_gcd(b, a % b)

def check_sequence_occurs(n, m, k, sequence):
    max_num = max(sequence)
    gcd_table = [[calculate_gcd(i, j) for j in range(1, m+1)] for i in range(1, n+1)]

    for i in range(n):
        for j in range(m-k+1):
            if gcd_table[i][j] == sequence[0]:
                found = True
                for l in range(1, k):
                    if gcd_table[i][j+l] != sequence[l]:
                        found = False
                        break
                if found:
                    return "YES"
    return "NO"

# Input
n, m, k = map(int, input().split())
sequence = list(map(int, input().split()))

# Output
print(check_sequence_occurs(n, m, k, sequence))
```
