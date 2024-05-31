
import math

def calculate_safety_factor(N, M, R, cars):
    # Initialize a list of lists to represent each lane
    lanes = [[] for _ in range(N)]
    
    for car in cars:
        lane_num, car_length, distance = car
        lanes[lane_num].append((car_length, distance))
    
    # Sort the cars in each lane based on their distances
    for lane in lanes:
        lane.sort(key=lambda x: x[1])
    
    # Calculate the maximum safety factor when switching lanes
    max_safety_factor = 0
    for _, distance in lanes[0]:
        min_dist_to_car = float('inf')
        
        # Check the potential position in the destination lane
        for dest_car_length, dest_distance in lanes[N-1]:
            if dest_distance >= distance:
                min_dist_to_car = min(min_dist_to_car, dest_distance - distance - dest_car_length)
        
        max_safety_factor = max(max_safety_factor, min_dist_to_car)
    
    if max_safety_factor == float('inf'):
        return "Impossible"
    
    return "{:.6f}".format(max_safety_factor)

# Sample Input Parsing
N, M, R = map(int, input().split())
cars = []
for _ in range(M):
    lane_num, car_length, distance = map(int, input().split())
    cars.append((lane_num, car_length, distance))

# Calculate and print the result
result = calculate_safety_factor(N, M, R, cars)
print(result)
