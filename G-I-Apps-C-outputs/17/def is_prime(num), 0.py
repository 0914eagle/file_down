
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def largest_prime_factor(arr):
    max_prime = 0
    for num in arr:
        for i in range(2, num+1):
            if num % i == 0 and is_prime(i):
                max_prime = max(max_prime, i)
    return max_prime

def partition_sequence(n, k, sequence):
    min_scores = []
    for i in range(n - k + 1):
        partition = sequence[i:i+k]
        min_scores.append(largest_prime_factor(partition))
    return min(min_scores)

input_data = input()
n, k = map(int, input_data.split())
sequence = list(map(int, input().split()))

max_score = partition_sequence(n, k, sequence)
print(max_score)
```
