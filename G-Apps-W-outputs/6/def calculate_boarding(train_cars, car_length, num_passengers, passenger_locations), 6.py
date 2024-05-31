
def calculate_boarding(train_cars, car_length, num_passengers, passenger_locations):
    max_walk_distance = 0
    max_passengers_boarding = 0
    
    for location in passenger_locations:
        closest_door = location % car_length
        walk_distance = min(closest_door, car_length - closest_door)
        max_walk_distance = max(max_walk_distance, walk_distance)
        
        car_number = location // car_length + 1
        
        passengers_boarding = train_cars - car_number + 1
        max_passengers_boarding = max(max_passengers_boarding, passengers_boarding)
    
    return max_walk_distance, max_passengers_boarding

# Input parsing
N, L, P = map(int, input().split())
passenger_locations = [int(input()) for _ in range(P)]

# Calculate and output result
result = calculate_boarding(N, L, P, passenger_locations)
print(result[0])
print(result[1])
