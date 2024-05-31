
def solve_train_boarding(N, L, P, passengers):
    distances = [L/2 - abs((L/2) - x) for x in passengers]
    max_distance = max(distances)
    
    car_occupancy = [0] * N
    for d in distances:
        car_idx = int(d // (L/2))
        car_occupancy[car_idx] += 1
    
    max_occupancy = max(car_occupancy)
    
    return int(max_distance), max_occupancy

# Input parsing
N, L, P = map(int, input().split())
passengers = [int(input()) for _ in range(P)]

# Solve the problem
max_distance, max_occupancy = solve_train_boarding(N, L, P, passengers)

# Output the result
print(max_distance)
print(max_occupancy)
