
def find_optimal_path(N, K, plants):
    dp = [0] * N
    parent = [-1] * N
    dp[0] = plants[0][2]  # Energy from eating flies at plant 1

    for i in range(1, N):
        dp[i] = float('-inf')
        for j in range(i):
            energy = dp[j] + plants[i][2] - K * (plants[i][0] - plants[j][0] + plants[i][1] - plants[j][1])
            if energy > dp[i]:
                dp[i] = energy
                parent[i] = j

    result = []
    idx = N - 1
    while idx != -1:
        result.append(idx)
        idx = parent[idx]
    result.reverse()

    return dp[N - 1], len(result), result

# Input processing
N, K = map(int, input().split())
plants = [list(map(int, input().split())) for _ in range(N)]

energy, path_len, path = find_optimal_path(N, K, plants)

# Output the results
print(energy)
print(path_len)
for idx in path:
    print(plants[idx][0], plants[idx][1])
