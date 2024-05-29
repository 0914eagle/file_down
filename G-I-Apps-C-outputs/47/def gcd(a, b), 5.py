
import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def is_sequence_in_table(n, m, k, sequence):
    for i in range(1, n+1):
        for j in range(1, m-k+2):
            found_sequence = True
            for l in range(k):
                if gcd(i, j+l) != sequence[l]:
                    found_sequence = False
                    break
            if found_sequence:
                return "YES"
    return "NO"

# Input reading
n, m, k = map(int, input().split())
sequence = list(map(int, input().split()))

# Check if the sequence occurs in table G
result = is_sequence_in_table(n, m, k, sequence)
print(result)
```
