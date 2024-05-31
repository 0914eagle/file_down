
def calculate_distances(N, L, P, passengers):
    max_distance = 0
    max_passengers = 0
    car_lengths = [L for _ in range(N)]
    
    for passenger in passengers:
        min_distance = float('inf')
        closest_car = -1
        
        for i, car_length in enumerate(car_lengths):
            door_position = car_length / 2
            distance = abs(passenger - door_position)
            
            if distance < min_distance:
                min_distance = distance
                closest_car = i
        
        if min_distance > max_distance:
            max_distance = min_distance
        
        car_lengths[closest_car] += L
        num_passengers_boarding = car_lengths[closest_car] // L
        
        if num_passengers_boarding > max_passengers:
            max_passengers = num_passengers_boarding
    
    return max_distance, max_passengers

# Input parsing
N, L, P = map(int, input().split())
passengers = [int(input()) for _ in range(P)]

# Calculate results
longest_distance, max_passengers_boarding = calculate_distances(N, L, P, passengers)

# Output the results
print(longest_distance)
print(max_passengers_boarding)
