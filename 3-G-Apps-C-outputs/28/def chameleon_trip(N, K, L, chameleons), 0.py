
def chameleon_trip(N, K, L, chameleons):
    trips = [0] * K
    positions = [0] * N
    colors = [0] * N
    directions = [0] * N
    
    for i in range(N):
        positions[i], colors[i], direction = chameleons[i]
        directions[i] = 1 if direction == 'D' else -1
    
    for i in range(N):
        for j in range(i+1, N):
            if directions[i] == directions[j]:
                continue
            distance = abs(positions[i] - positions[j])
            time = distance / 2
            color_i = colors[i]
            color_j = colors[j]
            if directions[i] == 1:
                trips[color_i] += time
                trips[(color_i + color_j) % K] += time
            else:
                trips[color_j] += time
                trips[(color_i + color_j) % K] += time
    
    return trips

# Input
N, K, L = map(int, input().split())
chameleons = []
for _ in range(N):
    d, b, direction = input().split()
    chameleons.append((int(d), int(b), direction))

# Output
trips = chameleon_trip(N, K, L, chameleons)
for trip in trips:
    print("{:.1f}".format(trip))
