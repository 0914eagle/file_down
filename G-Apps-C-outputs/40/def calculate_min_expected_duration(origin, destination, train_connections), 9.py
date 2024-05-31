
import math

def calculate_min_expected_duration(origin, destination, train_connections):
    n = len(train_connections)
    INF = 10**9
    dp = [[INF] * (n+1) for _ in range(n+1)]
    dp[0][0] = 0

    for i in range(n):
        for j in range(i+1):
            if dp[i][j] == INF:
                continue
            for k in range(j+1, n+1):
                if train_connections[i][1] == destination:
                    dp[i+1][k] = min(dp[i+1][k], dp[i][j] + train_connections[i][2])
                else:
                    p = train_connections[i][3] / 100
                    for delay in range(1, train_connections[i][4]+1):
                        dp[i+1][k] = min(dp[i+1][k], dp[i][j] + train_connections[i][2] + p*delay + (1-p)*train_connections[i][2])

    result = min(dp[n])
    return result if result != INF else "IMPOSSIBLE"

# Input parsing
origin, destination = input().split()
n = int(input())
train_connections = []
for _ in range(n):
    origin, destination, departure_time, duration, probability, max_delay = input().split()
    train_connections.append((origin, destination, int(departure_time), int(duration), int(probability), int(max_delay))

# Call the function and print the result
result = calculate_min_expected_duration(origin, destination, train_connections)
print(result)
