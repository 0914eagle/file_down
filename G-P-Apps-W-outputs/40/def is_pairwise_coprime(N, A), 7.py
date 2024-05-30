
import math

def is_pairwise_coprime(N, A):
    for i in range(N):
        for j in range(i+1, N):
            if math.gcd(A[i], A[j]) != 1:
                return "not coprime"
    return "pairwise coprime"

def is_setwise_coprime(N, A):
    if math.gcd(*A) == 1:
        return "setwise coprime"
    return is_pairwise_coprime(N, A)

# Input
N = int(input())
A = list(map(int, input().split()))

# Output
result = is_setwise_coprime(N, A)
print(result)
```
