
def calculate_safety_factor(N, M, R, cars):
    INF = float('inf')
    dp = [[-1 for _ in range(R + 1)] for _ in range(N)]
    dp[0][0] = 0
    
    for i in range(1, N):
        for j in range(R + 1):
            dp[i][j] = INF
            
    for i in range(1, N):
        for j in range(1, R + 1):
            for k in range(M):
                lane, length, dist = cars[k]
                if lane == i and dist <= j <= dist + length:
                    dp[i][j] = min(dp[i][j], max(dp[i-1][dj] + j - dist for dj in range(dist - length, j + 1)))
    
    result = min(dp[N-1])
    
    if result == INF:
        return "Impossible"
    else:
        return "{:.6f}".format(result)

# Sample Input parsing
input_line = input().strip().split()
N, M, R = map(int, input_line)
cars = []
for _ in range(M):
    car_line = input().strip().split()
    lane, length, dist = map(int, car_line)
    cars.append((lane, length, dist))

# Call function with input values
print(calculate_safety_factor(N, M, R, cars))
