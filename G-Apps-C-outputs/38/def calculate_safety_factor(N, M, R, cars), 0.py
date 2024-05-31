
import math

def calculate_safety_factor(N, M, R, cars):
    lane_cars = [[] for _ in range(N)]
    for car in cars:
        lane, length, distance = car
        lane_cars[lane].append((length, distance))

    def check_collision(i, j, d):
        if i < 0 or i >= len(lane_cars[j]):
            return False
        length, distance = lane_cars[j][i]
        return distance <= d <= distance + length

    def get_safety_factor(lane, d):
        left = right = math.inf
        for i in range(len(lane_cars[lane])):
            if check_collision(i, lane, d):
                return 0.0
            if i - 1 >= 0:
                left = min(left, lane_cars[lane][i][1] - (lane_cars[lane][i - 1][1] + lane_cars[lane][i - 1][0]))
            if i + 1 < len(lane_cars[lane]):
                right = min(right, lane_cars[lane][i + 1][1] - (lane_cars[lane][i][1] + lane_cars[lane][i][0]))

        return min(left, right)

    if len(lane_cars[0]) == 0:
        return "Impossible"

    max_safety_factor = math.inf
    for car in lane_cars[0]:
        d = car[1] + car[0]  # distance to back of the car
        safety_factor = get_safety_factor(N - 1, d)
        max_safety_factor = min(max_safety_factor, safety_factor)

    return "{:.6f}".format(max_safety_factor)

# Read input
N, M, R = map(int, input().split())
cars = [tuple(map(int, input().split())) for _ in range(M)]

# Calculate and output result
print(calculate_safety_factor(N, M, R, cars))
