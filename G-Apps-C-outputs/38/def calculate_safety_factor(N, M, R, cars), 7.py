
def calculate_safety_factor(N, M, R, cars):
    def find_closest_distance(lane, position):
        closest_distance = float('inf')
        for car_lane, car_length, car_position in cars:
            if car_lane == lane:
                if car_position + car_length >= position:
                    distance = car_position - position
                    closest_distance = min(closest_distance, distance)
        return closest_distance

    dp = [float('inf')] * (R + 1)
    dp[0] = 0

    for lane in range(1, N):
        for i in range(R, 0, -1):
            if dp[i] != float('inf'):
                for car_lane, car_length, car_position in cars:
                    if car_lane == lane:
                        if car_position <= i and i + car_length <= R:
                            dp[i + car_length] = min(dp[i + car_length], dp[i] + find_closest_distance(lane, i + car_length))

    result = min(dp)
    return result if result != float('inf') else "Impossible"

# Input parsing
N, M, R = map(int, input().split())
cars = [list(map(int, input().split())) for _ in range(M)]

# Calling the function
output = calculate_safety_factor(N, M, R, cars)
print(output)
