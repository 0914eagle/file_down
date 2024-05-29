
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_largest_prime_divisor(region):
    largest_prime = 0
    for num in region:
        if is_prime(num) and num > largest_prime:
            largest_prime = num
    return largest_prime

def find_max_score(n, k, sequence):
    max_score = 0
    for i in range(n - k + 1):
        region = sequence[i:i + k]
        largest_prime = find_largest_prime_divisor(region)
        max_score = max(max_score, largest_prime)
    return max_score

n, k = map(int, input().split())
sequence = list(map(int, input().split()))
result = find_max_score(n, k, sequence)
print(result)
```
