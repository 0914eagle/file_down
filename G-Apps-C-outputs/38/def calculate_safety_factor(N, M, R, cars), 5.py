
import sys

def calculate_safety_factor(N, M, R, cars):
    INF = float('inf')
    dp = [[INF] * (R + 1) for _ in range(N)]
    dp[0][0] = 0

    for i in range(1, M):
        lane, length, start = cars[i]
        for j in range(length, R + 1):
            dp[lane][j] = INF

    for i in range(1, M):
        lane, length, start = cars[i]
        for j in range(length, R + 1):
            for k in range(j - length, j):
                if dp[lane][k] != INF:
                    dp[lane][j] = min(dp[lane][j], max(dp[lane][k], start - k))

    result = min(dp[N-1])
    return result if result != INF else "Impossible"

# Read input
N, M, R = map(int, input().split())
cars = []
cars.append((0, 0, 0))  # ACM car

for _ in range(M):
    lane, length, start = map(int, input().split())
    cars.append((lane, length, start))

result = calculate_safety_factor(N, M, R, cars)
print(result)
