
def find_path(N, K, plants):
    dp = [[-1 for _ in range(K + 1)] for _ in range(N)]

    dp[0][K] = plants[0][2]

    for i in range(1, N):
        for j in range(K + 1):
            for k in range(i):
                if plants[k][0] < plants[i][0] or plants[k][1] < plants[i][1]:
                    energy = dp[k][j] + plants[i][2] - K
                    if energy >= 0 and energy + j >= 0 and energy + j <= K:
                        if dp[i][energy + j] < dp[k][j] + plants[i][2]:
                            dp[i][energy + j] = dp[k][j] + plants[i][2]
    
    max_energy = max(dp[N-1])
    path = []

    current_energy = dp[N-1].index(max_energy)
    current_plant = N-1

    while current_plant >= 0:
        if dp[current_plant][current_energy] == max_energy:
            path.append(current_plant)
            max_energy -= plants[current_plant][2]
            current_energy -= K
        current_plant -= 1

    path.reverse()

    return max_energy, len(path), [x + 1 for x in path]


# Input parsing
N, K = map(int, input().split())
plants = [list(map(int, input().split())) for _ in range(N)]

# Call the function and output the results
energy, num_plants, plant_path = find_path(N, K, plants)
print(energy)
print(num_plants)
for plant in plant_path:
    print(plants[plant-1][0], plants[plant-1][1])
