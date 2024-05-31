
def maximize_safety_factor(N, M, R, cars):
    lanes = [[] for _ in range(N)]
    for car in cars:
        lane, length, distance = car
        lanes[lane].append((length, distance))

    def check_safety_factor(lane_idx, start_pos):
        closest_distance = float('inf')
        for car_length, car_distance in lanes[lane_idx]:
            if car_distance <= start_pos <= car_distance + car_length:
                return 0.0
            closest_distance = min(closest_distance, abs(start_pos - car_distance - car_length/2))
        return closest_distance

    def can_switch(lane0_pos, lane1_pos):
        for car_length, car_distance in lanes[1]:
            if lane1_pos <= car_distance + car_length:
                return False
        return True

    safety_factors = []
    for lane0_length, lane0_distance in lanes[0]:
        for lane1_length, lane1_distance in lanes[1]:
            if lane1_distance >= lane0_length and can_switch(lane0_length, lane1_length):
                safety_factors.append(check_safety_factor(1, lane1_length))
    
    if safety_factors:
        return max(safety_factors)
    else:
        return "Impossible"

# Sample Input parsing
N, M, R = map(int, input().split())
cars = []
for _ in range(M):
    car_info = list(map(int, input().split()))
    cars.append(car_info)

# Call the function with the input
result = maximize_safety_factor(N, M, R, cars)
print(result)
