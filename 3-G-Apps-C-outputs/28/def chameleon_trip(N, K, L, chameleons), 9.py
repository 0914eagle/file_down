
def chameleon_trip(N, K, L, chameleons):
    trip_lengths = [0.0] * K
    positions = [0] * N
    colors = [0] * N
    directions = [''] * N

    for i in range(N):
        positions[i], colors[i], directions[i] = chameleons[i]

    for i in range(N):
        current_pos = positions[i]
        current_color = colors[i]
        current_direction = directions[i]

        if current_direction == 'D':
            trip_lengths[current_color] += L - current_pos
        else:
            trip_lengths[current_color] += current_pos

        for j in range(i + 1, N):
            next_pos = positions[j]
            next_color = colors[j]
            next_direction = directions[j]

            if current_direction == 'D' and next_direction == 'L':
                if current_color != next_color:
                    trip_lengths[current_color] += L - current_pos
                    trip_lengths[next_color] += next_pos
                    current_color = next_color
                else:
                    trip_lengths[current_color] += abs(next_pos - current_pos)
                break

            if current_direction == 'L' and next_direction == 'D':
                if current_color != next_color:
                    trip_lengths[current_color] += current_pos
                    trip_lengths[next_color] += L - next_pos
                    current_color = (current_color + next_color) % K
                else:
                    trip_lengths[current_color] += abs(next_pos - current_pos)
                break

    return trip_lengths

# Input
N, K, L = map(int, input().split())
chameleons = []
for _ in range(N):
    d, b, direction = input().split()
    chameleons.append((int(d), int(b), direction))

# Output
result = chameleon_trip(N, K, L, chameleons)
for trip_length in result:
    print("{:.1f}".format(trip_length))
