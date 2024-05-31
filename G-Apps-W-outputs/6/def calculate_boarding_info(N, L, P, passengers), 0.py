
def calculate_boarding_info(N, L, P, passengers):
    max_distance = 0
    max_boarding = 0
    doors = [L/2 + i*L for i in range(N)]
    boardings = [0] * N
    
    for p in passengers:
        min_distance = float('inf')
        closest_door = 0
        for i, door in enumerate(doors):
            distance = abs(p - door)
            if distance < min_distance:
                min_distance = distance
                closest_door = i
        
        if min_distance > max_distance:
            max_distance = min_distance
        boardings[closest_door] += 1
    
    max_boarding = max(boardings)
    
    return max_distance, max_boarding

# Read input values
N, L, P = map(int, input().split())
passengers = [int(input()) for _ in range(P)]

# Calculate and print the results
max_distance, max_boarding = calculate_boarding_info(N, L, P, passengers)
print(max_distance)
print(max_boarding)
