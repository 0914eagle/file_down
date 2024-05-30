
import math

def check_coprime(N, A):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    pairwise_coprime = True
    setwise_coprime = False

    for i in range(N):
        for j in range(i+1, N):
            if gcd(A[i], A[j]) != 1:
                pairwise_coprime = False
                break

    if not pairwise_coprime:
        gcd_all = A[0]
        for i in range(1, N):
            gcd_all = gcd(gcd_all, A[i])
        
        if gcd_all == 1:
            setwise_coprime = True

    if pairwise_coprime:
        print("pairwise coprime")
    elif setwise_coprime:
        print("setwise coprime")
    else:
        print("not coprime")

# Read input
N = int(input())
A = list(map(int, input().split()))

# Call the function with input values
check_coprime(N, A)
```
