
def punctual_city_train(N, L, P, passengers):
    car_lengths = [L / 2] * N
    max_distance = 0
    max_passengers = 0
    
    for passenger in passengers:
        min_distance = float('inf')
        closest_car = None
        
        for i, car in enumerate(car_lengths):
            distance_to_car = abs(passenger - car)
            if distance_to_car < min_distance or (distance_to_car == min_distance and i > closest_car):
                min_distance = distance_to_car
                closest_car = i
        
        car_lengths[closest_car] += L
        max_distance = max(max_distance, min_distance)
    
    max_passengers = max(car_lengths.count(L / 2), 1)
    
    return max_distance, max_passengers

# Read input
N, L, P = map(int, input().split())
passengers = [int(input()) for _ in range(P)]

# Call the function and output results
result_distance, result_passengers = punctual_city_train(N, L, P, passengers)
print(result_distance)
print(result_passengers)
