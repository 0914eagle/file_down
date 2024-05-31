
def punctual_city(N, L, P, passengers):
    passenger_distances = []
    for i in range(P):
        passenger_distances.append(passengers[i])

    max_distance = max(passenger_distances)
    max_passengers_per_car = 0

    for i in range(N):
        car_midpoint = (i + 0.5) * L
        passengers_boarding = sum(1 for dist in passenger_distances if abs(dist - car_midpoint) <= L/2)
        max_passengers_per_car = max(max_passengers_per_car, passengers_boarding)

    longest_distance = max_distance - (N-1) * L/2
    print(int(longest_distance))
    print(max_passengers_per_car)

# Input parsing
N, L, P = map(int, input().split())
passengers = [int(input()) for _ in range(P)]

# Function call
punctual_city(N, L, P, passengers)
