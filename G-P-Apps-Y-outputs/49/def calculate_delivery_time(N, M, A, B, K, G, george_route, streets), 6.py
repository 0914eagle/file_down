
def calculate_delivery_time(N, M, A, B, K, G, george_route, streets):
    george_time = 0
    for i in range(len(george_route)-1):
        for j in range(len(streets)):
            if (george_route[i], george_route[i+1]) == (streets[j][0], streets[j][1]) or (george_route[i+1], george_route[i]) == (streets[j][0], streets[j][1]):
                george_time += streets[j][2]

    arrival_time = [(K+i) % 1440 for i in range(george_time+1)]

    dp = [float('inf')] * N
    dp[A-1] = 0

    for i in range(george_time):
        new_dp = [float('inf')] * N
        for j in range(M):
            a, b, l = streets[j]
            new_dp[b-1] = min(new_dp[b-1], dp[a-1] + l)

        dp = new_dp

    return min(dp[i] + arrival_time[i] for i in range(N)) + george_time

# Reading input
N, M = map(int, input().split())
A, B, K, G = map(int, input().split())
george_route = list(map(int, input().split()))
streets = []
for _ in range(M):
    a, b, l = map(int, input().split())
    streets.append((a, b, l))

# Calculating delivery time
delivery_time = calculate_delivery_time(N, M, A, B, K, G, george_route, streets)

# Output
print(delivery_time)
```
