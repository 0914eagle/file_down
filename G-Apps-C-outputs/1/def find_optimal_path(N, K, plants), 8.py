
def find_optimal_path(N, K, plants):
    energy_levels = [0] * N
    jump_from = [-1] * N

    energy_levels[0] = plants[0][2]  # Energy from eating flies at plant 1

    for i in range(1, N):
        energy_levels[i] = float('-inf')
        for j in range(i):
            cost = K * (abs(plants[i][0] - plants[j][0]) + abs(plants[i][1] - plants[j][1]))
            new_energy = energy_levels[j] + plants[i][2] - cost
            if new_energy > energy_levels[i]:
                energy_levels[i] = new_energy
                jump_from[i] = j

    optimal_path = [N]
    current = N - 1
    while current != 0:
        optimal_path.append(jump_from[current] + 1)
        current = jump_from[current]

    optimal_path.append(1)
    optimal_path.reverse()

    return energy_levels[N - 1], len(optimal_path), optimal_path

# Input processing
N, K = map(int, input().split())
plants = []
for _ in range(N):
    X, Y, F = map(int, input().split())
    plants.append((X, Y, F))

# Find the optimal path
energy_level, num_plants, optimal_path = find_optimal_path(N, K, plants)

# Output the results
print(energy_level)
print(num_plants)
for plant in optimal_path:
    print(f"{plants[plant-1][0]} {plants[plant-1][1]}")
