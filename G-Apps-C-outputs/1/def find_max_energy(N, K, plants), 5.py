
def find_max_energy(N, K, plants):
    energy = [0] * N
    jumps = [0] * N
    energy[0] = plants[0][2]  # Initial energy from flies around plant 1

    for i in range(1, N):
        max_energy = 0
        prev_jump = -1
        for j in range(i):
            cost = abs(plants[i][0] - plants[j][0]) + abs(plants[i][1] - plants[j][1])
            if (plants[i][0] > plants[j][0] and plants[i][1] == plants[j][1]) or (plants[i][1] > plants[j][1] and plants[i][0] == plants[j][0]):
                if energy[j] >= cost * K and energy[j] > max_energy:
                    max_energy = energy[j]
                    prev_jump = j

        if prev_jump != -1:
            energy[i] = max_energy + plants[i][2]
            jumps[i] = prev_jump

    max_energy = max(energy)
    path = []
    current = energy.index(max_energy)
    while current >= 0:
        path.append(current+1)
        current = jumps[current]

    path.reverse()
    return max_energy, len(path), path


# Read input
N, K = map(int, input().split())
plants = [list(map(int, input().split())) for _ in range(N)]

# Find the sequence of plants to maximize energy
max_energy, num_plants, plant_sequence = find_max_energy(N, K, plants)

# Print output
print(max_energy)
print(num_plants)
for plant in plant_sequence:
    print(plants[plant-1][0], plants[plant-1][1])
