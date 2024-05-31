
import math

def is_perfect_square(num):
    root = math.isqrt(num)
    return root ** 2 == num

def shortest_subsequence_with_perfect_square(n, arr):
    factors = [[] for _ in range(n)]
    for i in range(n):
        for j in range(1, int(math.sqrt(arr[i])) + 1):
            if arr[i] % j == 0:
                factors[i].append(j)
                if j != arr[i] // j:
                    factors[i].append(arr[i] // j)

    for i in range(n):
        for j in range(i):
            common_factors = set(factors[i]) & set(factors[j])
            if any(is_perfect_square(num) for num in common_factors):
                return 2

    for i in range(n):
        if is_perfect_square(arr[i]):
            return 1

    return 3

# Input processing
n = int(input())
arr = list(map(int, input().split()))

# Output
print(shortest_subsequence_with_perfect_square(n, arr))
