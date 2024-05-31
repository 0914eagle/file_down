
def solve_frog_energy(N, K, plants):
    dp = [(0, 0) for _ in range(N)]
    for i in range(1, N):
        max_energy = 0
        prev_plant = -1
        for j in range(i):
            energy = plants[i][2] + dp[j][0] - K * (plants[i][0] - plants[j][0] + plants[i][1] - plants[j][1])
            if energy > max_energy:
                max_energy = energy
                prev_plant = j
        dp[i] = (max_energy, prev_plant)
    
    result = []
    energy = dp[N-1][0]
    current_plant = N - 1
    while current_plant >= 0:
        result.append(current_plant)
        current_plant = dp[current_plant][1]
    
    result.reverse()
    
    return energy, len(result), result

# Input parsing
N, K = map(int, input().split())
plants = []
for _ in range(N):
    x, y, f = map(int, input().split())
    plants.append((x, y, f))

# Solve the problem
energy, L, sequence = solve_frog_energy(N, K, plants)

# Output the result
print(energy)
print(L)
for plant in sequence:
    print(plant + 1)
