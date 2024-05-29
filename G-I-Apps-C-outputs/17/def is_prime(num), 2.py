
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def largest_prime_divisor(arr):
    max_prime_divisor = 0
    for num in arr:
        for i in range(2, num + 1):
            if is_prime(i) and num % i == 0 and i > max_prime_divisor:
                max_prime_divisor = i
    return max_prime_divisor

def max_score_partition(n, k, sequence):
    max_score = 0
    for start in range(n - k + 1):
        partition = sequence[start:start+k]
        max_score = max(max_score, largest_prime_divisor(partition))
    return max_score

# Read input
n, k = map(int, input().split())
sequence = list(map(int, input().split()))

# Calculate and print output
print(max_score_partition(n, k, sequence))
```
