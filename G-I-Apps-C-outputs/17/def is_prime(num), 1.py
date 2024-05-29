
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_largest_prime_divisor(arr):
    max_prime = 0
    for num in arr:
        for i in range(num, 1, -1):
            if is_prime(i) and all(num % j == 0 for j in arr):
                max_prime = max(max_prime, i)
    return max_prime

def maximize_score(n, k, sequence):
    max_score = 0
    for i in range(n - k + 1):
        region = sequence[i:i+k]
        score = find_largest_prime_divisor(region)
        max_score = max(max_score, score)
    return max_score

# Input
n, k = map(int, input().split())
sequence = list(map(int, input().split()))

# Output
print(maximize_score(n, k, sequence))
```
