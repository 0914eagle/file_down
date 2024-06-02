
def chameleon_trip(N, K, L, chameleons):
    trips = [0.0] * K
    positions = [0] * N
    colors = [0] * N
    directions = [0] * N
    
    for i in range(N):
        positions[i], colors[i], direction = chameleons[i]
        directions[i] = 1 if direction == 'D' else -1
    
    for i in range(N):
        total_distance = 0
        current_color = colors[i]
        current_direction = directions[i]
        
        for j in range(i, N):
            if colors[j] == current_color:
                total_distance += abs(positions[j] - positions[i])
                positions[j] = positions[i]
            else:
                total_distance += abs(positions[j] - positions[i])
                positions[j] = positions[i]
                current_color = (current_color + colors[j]) % K
                current_direction *= -1
        
        trips[current_color] += total_distance
    
    return trips

# Input
N, K, L = map(int, input().split())
chameleons = []
for _ in range(N):
    d, b, direction = input().split()
    chameleons.append((int(d), int(b), direction))

# Output
result = chameleon_trip(N, K, L, chameleons)
for trip in result:
    print(f"{trip:.1f}")
