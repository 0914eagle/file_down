
def calculate_safety_factor(N, M, R, cars):
    cars.sort(key=lambda x: (x[0], x[2]))  # Sort cars by lane number and distance

    lane_cars = [[] for _ in range(N)]  # Initialize list of cars in each lane
    for car in cars:
        lane_cars[car[0]].append(car)

    dp = [[float('inf')] * N for _ in range(M)]  # Initialize dynamic programming table

    for i in range(N):
        if i == 0:
            dp[0][i] = cars[0][2]  # Initialize first row with distances to the back of the cars in lane 0
        else:
            break

    for i in range(1, M):
        for j in range(N):
            if j == 0:
                dp[i][j] = min(dp[i-1][j], cars[i][2])  # ACM car can only be in lane 0
            else:
                dp[i][j] = min(dp[i-1][j], min(dp[i-1][j-1], cars[i][2]))  # Update safety factor

    return dp[-1][-1] if dp[-1][-1] != float('inf') else "Impossible"

# Input
N, M, R = map(int, input().split())
cars = [list(map(int, input().split())) for _ in range(M)]

# Output
result = calculate_safety_factor(N, M, R, cars)
print(result)
