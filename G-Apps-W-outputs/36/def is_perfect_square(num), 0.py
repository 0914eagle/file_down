
from math import sqrt

def is_perfect_square(num):
    return int(sqrt(num))**2 == num

def shortest_subsequence_length(n, arr):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]  # List of prime numbers with 7 or fewer divisors
    
    dp = {1: 0}  # Dictionary to store the length of the shortest subsequence with product as key
    for num in arr:
        for key in list(dp.keys()):
            new_product = key * num
            new_length = dp[key] + 1
            if is_perfect_square(new_product):
                return new_length
            if new_product not in dp and all(new_product % prime != 0 for prime in primes):
                dp[new_product] = new_length
    
    return -1

# Input parsing
n = int(input())
arr = list(map(int, input().split()))

# Output
print(shortest_subsequence_length(n, arr))
