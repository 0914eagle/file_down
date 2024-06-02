
def chameleon_trip(N, K, L, chameleons):
    trips = [0] * K
    positions = [0] * N
    colors = [0] * N
    directions = [0] * N

    for i in range(N):
        positions[i], colors[i], direction = chameleons[i]
        directions[i] = 1 if direction == 'D' else -1

    for i in range(N):
        for j in range(i + 1, N):
            if directions[i] == directions[j]:
                continue
            if directions[i] == 1 and directions[j] == -1:
                if colors[i] == colors[j]:
                    continue
                new_color = (colors[i] + colors[j]) % K
                trips[colors[i]] += L - abs(positions[i] - positions[j])
                trips[colors[j]] += L - abs(positions[i] - positions[j])
                colors[i] = new_color
                colors[j] = new_color
            else:
                trips[colors[i]] += abs(positions[i] - positions[j])
                trips[colors[j]] += abs(positions[i] - positions[j])

    return trips

# Input parsing
N, K, L = map(int, input().split())
chameleons = []
for _ in range(N):
    d, b, direction = input().split()
    chameleons.append((int(d), int(b), direction))

# Calculate and print the total trip taken by the chameleons in each color
trips = chameleon_trip(N, K, L, chameleons)
for trip in trips:
    print("{:.1f}".format(trip))

