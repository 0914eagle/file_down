
from collections import Counter

def is_perfect_square(n):
    sqrt_n = int(n ** 0.5)
    return sqrt_n * sqrt_n == n

def shortest_perfect_square_subsequence(n, arr):
    freq = Counter(arr)
    for num in arr:
        for factor in range(2, int(num ** 0.5) + 1):
            if num % (factor * factor) == 0:
                freq[num] = max(freq[num], freq.get(factor, 0), freq.get(num // factor, 0)) + 1

    shortest_length = float('inf')
    for num, count in freq.items():
        if is_perfect_square(num):
            shortest_length = min(shortest_length, n - count)

    return shortest_length if shortest_length != float('inf') and shortest_length > 0 else -1

# Input reading
n = int(input())
arr = list(map(int, input().split()))

# Output
print(shortest_perfect_square_subsequence(n, arr))
