
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_largest_prime_factor(nums):
    largest_prime_factor = 0
    for num in nums:
        if is_prime(num) and num > largest_prime_factor:
            largest_prime_factor = num
    return largest_prime_factor

def max_score_partition(n, k, sequence):
    max_score = 0
    for i in range(n - k + 1):
        region = sequence[i:i+k]
        largest_prime_factor = find_largest_prime_factor(region)
        if largest_prime_factor > max_score:
            max_score = largest_prime_factor
    return max_score

# Input parsing
n, k = map(int, input().split())
sequence = list(map(int, input().split()))

# Call the function and output the result
print(max_score_partition(n, k, sequence))
```
