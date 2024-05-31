
def calculate_distance_and_max_passengers(N, L, P, positions):
    positions.sort()
    
    max_distance = 0
    max_passengers = 0
    
    for i in range(P):
        car_number = min((positions[i] + L // 2) // L + 1, N)
        distance = car_number * L - L // 2 - positions[i]
        max_distance = max(max_distance, distance)
        
    car_count = [0] * N
    for i in range(P):
        car_number = min((positions[i] + L // 2) // L + 1, N)
        car_count[car_number - 1] += 1
        max_passengers = max(max_passengers, car_count[car_number - 1])
        
    return max_distance, max_passengers

# Input
N, L, P = map(int, input().split())
positions = [int(input()) for _ in range(P)]

# Output
max_distance, max_passengers = calculate_distance_and_max_passengers(N, L, P, positions)
print(max_distance)
print(max_passengers)
