
def chameleon_trip(N, K, L, chameleons):
    positions = [0] * K
    colors = [0] * K
    distances = [0] * K
    directions = [0] * K
    for d, b, direction in chameleons:
        positions[b] = d
        colors[b] = b
        distances[b] = d
        directions[b] = 1 if direction == 'D' else -1
    
    total_trips = [0] * K
    for i in range(K):
        total_trip = 0
        for j in range(K):
            if colors[i] == colors[j]:
                continue
            if directions[i] == directions[j]:
                total_trip += abs(positions[i] - positions[j])
            else:
                total_trip += L - abs(positions[i] - positions[j])
        total_trips[colors[i]] = total_trip
    
    return total_trips

# Input
N, K, L = map(int, input().split())
chameleons = [list(map(str, input().split())) for _ in range(N)]

# Output
result = chameleon_trip(N, K, L, chameleons)
for trip in result:
    print("{:.1f}".format(trip))
