
import math

def minimum_planes(n, m, inspection_times, flight_times, flights):
    INF = float('inf')

    dp = [[INF] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                dp[i][j] = flight_times[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    planes = 0
    for flight in flights:
        start, end, time = flight
        start -= 1
        end -= 1
        min_inspection_time = inspection_times[start]
        departure_time = time + dp[start][end]
        if departure_time > min_inspection_time:
            planes += 1

    return planes

# Input parsing
n, m = map(int, input().split())
inspection_times = list(map(int, input().split()))
flight_times = [list(map(int, input().split())) for _ in range(n)]
flights = [list(map(int, input().split())) for _ in range(m)]

# Call the function and print the result
result = minimum_planes(n, m, inspection_times, flight_times, flights)
print(result)
