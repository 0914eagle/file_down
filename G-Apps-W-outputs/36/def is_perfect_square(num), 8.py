
import math

def is_perfect_square(num):
    sqrt_num = int(math.sqrt(num))
    return sqrt_num * sqrt_num == num

def factors_count(num):
    count = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            if num // i == i:
                count += 1
            else:
                count += 2
    return count

def shortest_subsequence_length(n, arr):
    dp = [set() for _ in range(n)]
    result = float('inf')

    for i in range(n):
        dp[i].add(arr[i])
        if is_perfect_square(arr[i]):
            result = 1

    for i in range(1, n):
        for j in range(i):
            new_num = arr[i] * arr[j]
            if new_num <= 10 ** 6:
                num_divisors = factors_count(new_num)
                if num_divisors <= 7:
                    dp[i].add(new_num)
                    dp[i] = dp[i].union(dp[j])
                    if is_perfect_square(new_num):
                        result = min(result, len(dp[i]))

    return result if result != float('inf') else -1

# Input parsing
n = int(input())
arr = list(map(int, input().split()))

# Output
print(shortest_subsequence_length(n, arr))
