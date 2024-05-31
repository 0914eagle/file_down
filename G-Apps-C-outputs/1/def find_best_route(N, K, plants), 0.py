
def find_best_route(N, K, plants):
    energy_levels = [0] * N
    jumps = [0] * N
    energy_levels[0] = plants[0][2]

    for i in range(1, N):
        max_energy = 0
        best_jump = -1

        for j in range(i):
            energy_gain = plants[i][2]
            energy_cost = abs(plants[i][0] - plants[j][0]) + abs(plants[i][1] - plants[j][1]) * K

            if energy_cost <= energy_levels[j] and energy_levels[j] - energy_cost + energy_gain > max_energy:
                max_energy = energy_levels[j] - energy_cost + energy_gain
                best_jump = j

        energy_levels[i] = max_energy
        jumps[i] = best_jump

    result = []
    current_index = N - 1
    while current_index != 0:
        result.append(current_index + 1)
        current_index = jumps[current_index]

    result.append(1)
    result.reverse()

    return energy_levels[N - 1], len(result), result


# Input processing
N, K = map(int, input().split())
plants = []
for _ in range(N):
    x, y, f = map(int, input().split())
    plants.append((x, y, f))

# Call the function and output the result
energy, num_plants, route = find_best_route(N, K, plants)
print(energy)
print(num_plants)
for plant in route:
    print(plant)
