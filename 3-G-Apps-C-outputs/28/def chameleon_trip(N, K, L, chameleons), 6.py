
def chameleon_trip(N, K, L, chameleons):
    trips = [0.0] * K
    positions = [0] * N
    colors = [0] * N
    directions = [''] * N
    
    for i, (d, b, direction) in enumerate(chameleons):
        positions[i] = d
        colors[i] = b
        directions[i] = direction
    
    for i in range(N):
        distance = L if directions[i] == 'R' else positions[i]
        trips[colors[i]] += distance
    
    for i in range(N-1):
        if directions[i] == 'R' and directions[i+1] == 'L':
            trips[colors[i]] += L - (positions[i] + 1) + positions[i+1]
            trips[(colors[i] + colors[i+1]) % K] += L - (positions[i] + 1) + positions[i+1]
    
    return trips

# Input processing
N, K, L = map(int, input().split())
chameleons = []
for _ in range(N):
    d, b, direction = input().split()
    d = int(d)
    b = int(b)
    chameleons.append((d, b, direction))

# Calculate and output the total trip taken by chameleons in each color
trips = chameleon_trip(N, K, L, chameleons)
for trip in trips:
    print("{:.1f}".format(trip))
