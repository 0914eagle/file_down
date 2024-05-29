
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def check_sequence_occurrence(n, m, k, a):
    max_gcd = math.gcd(n, m)
    
    for i in range(1, min(n, max_gcd) + 1):
        if n % i == 0 and m % i == 0:
            if all(gcd(i, j) == a[j-1] for j in range(1, k+1)):
                return "YES"
            
    return "NO"

n, m, k = map(int, input().split())
a = list(map(int, input().split()))

print(check_sequence_occurrence(n, m, k, a))
```
