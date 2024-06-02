
import math

def is_coprime(a, b):
    return math.gcd(a, b) == 1

def make_co_prime_array(n, arr):
    result = []
    moves = 0
    
    for i in range(n-1):
        result.append(arr[i])
        if not is_coprime(arr[i], arr[i+1]):
            gcd = math.gcd(arr[i], arr[i+1])
            result.append(gcd+1)
            moves += 1
    
    result.append(arr[-1])
    
    print(moves)
    print(" ".join(map(str, result)))

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
make_co_prime_array(n, arr)
