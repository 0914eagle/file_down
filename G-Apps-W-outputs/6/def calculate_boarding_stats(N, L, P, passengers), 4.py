
def calculate_boarding_stats(N, L, P, passengers):
    max_distance = 0
    max_boarding = 0
    car_length = L / 2

    distances = []
    for passenger in passengers:
        distance_to_closest_door = min(passenger, L - passenger)
        distances.append(distance_to_closest_door)

    max_distance = max(distances)
    max_boarding = distances.count(max_distance)

    return max_distance, max_boarding

# Input parsing
N, L, P = map(int, input().split())
passengers = [int(input()) for _ in range(P)]

# Calculate boarding statistics
longest_distance, max_boarding_count = calculate_boarding_stats(N, L, P, passengers)

# Output
print(longest_distance)
print(max_boarding_count)
