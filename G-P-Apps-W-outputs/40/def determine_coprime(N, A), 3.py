
import math

def determine_coprime(N, A):
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
        if gcd(*A) == 1:
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

# Call the function
determine_coprime(N, A)
```
