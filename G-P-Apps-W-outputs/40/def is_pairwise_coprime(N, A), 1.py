
import math

def is_pairwise_coprime(N, A):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    for i in range(N):
        for j in range(i+1, N):
            if gcd(A[i], A[j]) != 1:
                return "not coprime"

    return "pairwise coprime"

N = int(input())
A = list(map(int, input().split()))

result = is_pairwise_coprime(N, A)
if result == "not coprime":
    if math.gcd(*A) == 1:
        print("setwise coprime")
    else:
        print("not coprime")
else:
    print(result)
```
