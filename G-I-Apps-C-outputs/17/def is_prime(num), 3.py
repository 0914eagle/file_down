
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_largest_prime_factor(nums):
    max_prime = 0
    for num in nums:
        if is_prime(num) and num > max_prime:
            max_prime = num
    return max_prime

def find_maximum_score(n, k, sequence):
    max_score = 0
    for i in range(n - k + 1):
        score = find_largest_prime_factor(sequence[i:i+k])
        if score > max_score:
            max_score = score
    return max_score

# Input processing
n, k = map(int, input().split())
sequence = list(map(int, input().split()))

# Call the function to find maximum score
max_score = find_maximum_score(n, k, sequence)
print(max_score)
```
