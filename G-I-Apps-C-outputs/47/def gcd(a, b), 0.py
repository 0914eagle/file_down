
import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def is_sequence_in_table(n, m, k, sequence):
    for i in range(k):
        if gcd(sequence[i], sequence[i+1]) != sequence[i]:
            return "NO"
    
    for i in range(n):
        for j in range(m - k + 1):
            found = True
            for l in range(k):
                if gcd(i+1, j+l+1) != sequence[l]:
                    found = False
                    break
            if found:
                return "YES"
    
    return "NO"

# Input handling
n, m, k = map(int, input().split())
sequence = list(map(int, input().split()))

# Check if the sequence occurs in table G
result = is_sequence_in_table(n, m, k, sequence)
print(result)
```
