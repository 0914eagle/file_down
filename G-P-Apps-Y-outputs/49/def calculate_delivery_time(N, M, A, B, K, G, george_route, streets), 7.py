
def calculate_delivery_time(N, M, A, B, K, G, george_route, streets):
    george_time = {}  # Dictionary to store the time range for each street on George's route
    for i in range(len(george_route) - 1):
        street = (george_route[i], george_route[i + 1])
        george_time[street] = (i * 2, i * 2 + streets[street])

    min_time = float('inf')  # Initialize minimum time needed to a large value
    for intersection in range(1, N + 1):
        if intersection != A:
            luka_time = K  # Luka starts at A K minutes after George
            for street in george_time.values():
                # Calculate the time Luka can enter each street
                if street[0] <= luka_time <= street[1]:
                    luka_time = street[1] + 1
                luka_time += abs(intersection - A)  # Time to reach the intersection
            luka_time += abs(intersection - B)  # Time to reach destination
            min_time = min(min_time, luka_time)

    return min_time

# Read input
N, M = map(int, input().split())
A, B, K, G = map(int, input().split())
george_route = list(map(int, input().split()))
streets = {}
for _ in range(M):
    A, B, L = map(int, input().split())
    streets[(A, B)] = L

# Calculate and output the least amount of time Luka needs to make his delivery
print(calculate_delivery_time(N, M, A, B, K, G, george_route, streets))
```
