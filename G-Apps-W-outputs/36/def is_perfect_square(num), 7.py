
import math

def is_perfect_square(num):
    sqrt_num = int(math.sqrt(num))
    return num == sqrt_num * sqrt_num

def shortest_subsequence_with_perfect_square(n, a):
    dp = [0] * (1 << 7)
    dp[0] = 1

    for num in a:
        mask = 0
        for i in range(1, 8):
            if num % i == 0:
                mask |= 1 << (i - 1)

        for i in range(len(dp) - 1, -1, -1):
            if dp[i] > 0:
                dp[i | mask] = max(dp[i | mask], dp[i] + 1)

    for i in range(len(dp)):
        if dp[i] > 1 and is_perfect_square(i):
            return dp[i] - 1

    return -1

# Input processing
n = int(input())
a = list(map(int, input().split()))

# Output
print(shortest_subsequence_with_perfect_square(n, a))
