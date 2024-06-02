
def calculate_trip_lengths(N, K, L, chameleons):
    trip_lengths = [0.0] * K
    positions = [chameleon[0] for chameleon in chameleons]
    colors = [chameleon[1] for chameleon in chameleons]
    directions = [chameleon[2] for chameleon in chameleons]

    for i in range(N):
        if directions[i] == 'D':
            distance_to_end = L - positions[i]
        else:
            distance_to_end = positions[i]

        trip_lengths[colors[i]] += distance_to_end

        for j in range(i + 1, N):
            if directions[i] != directions[j]:
                if directions[i] == 'D':
                    new_color = (colors[i] + colors[j]) % K
                    trip_lengths[colors[i]] += distance_to_end
                    trip_lengths[colors[j]] += distance_to_end
                    trip_lengths[new_color] += L - distance_to_end
                else:
                    new_color = (colors[i] + colors[j]) % K
                    trip_lengths[colors[i]] += distance_to_end
                    trip_lengths[colors[j]] += distance_to_end
                    trip_lengths[new_color] += L - distance_to_end
                break

    return trip_lengths

# Input parsing
N, K, L = map(int, input().split())
chameleons = []
for _ in range(N):
    d, b, direction = input().split()
    chameleons.append((int(d), int(b), direction))

# Calculate and print trip lengths
trip_lengths = calculate_trip_lengths(N, K, L, chameleons)
for length in trip_lengths:
    print("{:.1f}".format(length))
