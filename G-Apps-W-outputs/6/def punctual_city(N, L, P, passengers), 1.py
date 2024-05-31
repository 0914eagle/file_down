
def punctual_city(N, L, P, passengers):
    car_length = L / 2
    max_walk_distance = 0
    max_passengers_boarding_car = 0

    car_boarding_counts = [0] * N

    for passenger in passengers:
        closest_car = int(passenger // car_length)
        if closest_car == N:
            closest_car -= 1
        
        walk_distance = min(passenger - closest_car * car_length, (closest_car + 1) * car_length - passenger)
        max_walk_distance = max(max_walk_distance, walk_distance)
        
        car_boarding_counts[closest_car] += 1

    max_passengers_boarding_car = max(car_boarding_counts)

    return max_walk_distance, max_passengers_boarding_car

# Input parsing
N, L, P = map(int, input().split())
passengers = [int(input()) for _ in range(P)]

# Call the function and print the output
max_walk_distance, max_passengers_boarding_car = punctual_city(N, L, P, passengers)
print(max_walk_distance)
print(max_passengers_boarding_car)
