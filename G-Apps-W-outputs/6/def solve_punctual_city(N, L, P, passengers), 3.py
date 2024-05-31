
def solve_punctual_city(N, L, P, passengers):
    max_distance = 0
    max_passengers = 0
    car_lengths = [L / 2 + (i * L) for i in range(N)]  # Calculate the position of each door

    for passenger in passengers:
        min_distance = float('inf')
        closest_car = -1
        for i, car in enumerate(car_lengths):
            distance = abs(car - passenger)
            if distance < min_distance or (distance == min_distance and i > closest_car):
                min_distance = distance
                closest_car = i
        
        max_distance = max(max_distance, min_distance)
        max_passengers = max(max_passengers, passengers.count(passenger))

    return max_distance, max_passengers

# Input
N, L, P = map(int, input().split())
passengers = [int(input()) for _ in range(P)]

# Solve and output
max_distance, max_passengers = solve_punctual_city(N, L, P, passengers)
print(max_distance)
print(max_passengers)
