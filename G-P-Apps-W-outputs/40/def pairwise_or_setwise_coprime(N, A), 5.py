
import math

def pairwise_or_setwise_coprime(N, A):
    pairwise = True
    for i in range(N):
        for j in range(i+1, N):
            if math.gcd(A[i], A[j]) != 1:
                pairwise = False
                break
    if pairwise:
        print("pairwise coprime")
    else:
        if math.gcd(*A) == 1:
            print("setwise coprime")
        else:
            print("not coprime")

# Sample Input
N = 3
A = [3, 4, 5]
pairwise_or_setwise_coprime(N, A)
```

