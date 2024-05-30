
import math

def is_pairwise_coprime(arr):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if gcd(arr[i], arr[j]) != 1:
                return False
    return True

def is_setwise_coprime(arr):
    gcd_all = arr[0]
    for num in arr[1:]:
        gcd_all = math.gcd(gcd_all, num)
    return gcd_all == 1

# Read input
N = int(input())
A = list(map(int, input().split()))

# Check if pairwise coprime
if is_pairwise_coprime(A):
    print("pairwise coprime")
# Check if setwise coprime
elif is_setwise_coprime(A):
    print("setwise coprime")
else:
    print("not coprime")
```
