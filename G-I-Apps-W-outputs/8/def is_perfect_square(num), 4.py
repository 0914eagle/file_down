
from math import isqrt

def is_perfect_square(num):
    return isqrt(num)**2 == num

def shortest_subsequence_with_perfect_square(n, arr):
    prime_factors = [0] * (10**6 + 1)

    for num in arr:
        for i in range(2, isqrt(num) + 1):
            while num % i == 0:
                prime_factors[i] += 1
                num //= i
        if num > 1:
            prime_factors[num] += 1

    for num in arr:
        temp_factors = list(prime_factors)
        for i in range(2, isqrt(num) + 1):
            while num % i == 0:
                temp_factors[i] -= 1
                num //= i
        if num > 1:
            temp_factors[num] -= 1

        for i in range(2, len(temp_factors)):
            if temp_factors[i] % 2 != 0:
                break
        else:
            return 1
    
    for i in range(2, len(prime_factors)):
        if prime_factors[i] % 2 == 0 and prime_factors[i] > 0:
            return 1
    
    return 2

# Input processing
n = int(input())
arr = list(map(int, input().split()))

# Output
result = shortest_subsequence_with_perfect_square(n, arr)
print(result)
