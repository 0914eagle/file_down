
import math

def is_pairwise_coprime(N, arr):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    for i in range(N):
        for j in range(i + 1, N):
            if gcd(arr[i], arr[j]) != 1:
                return "not coprime"
    
    return "pairwise coprime"

N = int(input())
arr = list(map(int, input().split()))

result = is_pairwise_coprime(N, arr)
if result == "not coprime":
    if math.gcd(*arr) == 1:
        print("setwise coprime")
    else:
        print(result)
else:
    print(result)
```
