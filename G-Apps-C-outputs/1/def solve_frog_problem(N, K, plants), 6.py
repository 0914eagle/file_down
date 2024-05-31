
def solve_frog_problem(N, K, plants):
    energy_levels = [0] * N
    jumps = [0] * N
    energy_levels[0] = plants[0][2]
    
    for i in range(1, N):
        max_energy = 0
        max_energy_jump = 0
        for j in range(i):
            energy = energy_levels[j] - K * (plants[i][0] - plants[j][0] + plants[i][1] - plants[j][1])
            if energy >= max_energy:
                max_energy = energy
                max_energy_jump = j
        energy_levels[i] = max_energy + plants[i][2]
        jumps[i] = max_energy_jump
    
    path = []
    curr = N - 1
    while curr != 0:
        path.append(curr)
        curr = jumps[curr]
    path.append(0)
    path.reverse()
    
    return energy_levels[N - 1], len(path), [plants[i][:2] for i in path]

# Input parsing
N, K = map(int, input().split())
plants = []
for _ in range(N):
    X, Y, F = map(int, input().split())
    plants.append((X, Y, F))

result = solve_frog_problem(N, K, plants)
print(result[0])
print(result[1])
for p in result[2]:
    print(p[0], p[1])
