
def find_optimal_path(N, K, plants):
    dp = [(0, 0) for _ in range(N)]
    dp[0] = (plants[0][2], 0)
    
    for i in range(1, N):
        dp[i] = (plants[i][2], i)
        for j in range(i):
            cost = abs(plants[i][0] - plants[j][0]) + abs(plants[i][1] - plants[j][1])
            if plants[j][2] >= cost * K and dp[j][0] + plants[i][2] > dp[i][0]:
                dp[i] = (dp[j][0] + plants[i][2], j)
    
    path = []
    idx = N - 1
    while idx != 0:
        path.append(idx)
        idx = dp[idx][1]
    path.append(0)
    
    path.reverse()
    return dp[N-1][0], len(path), path

# Read input
N, K = map(int, input().split())
plants = [tuple(map(int, input().split())) for _ in range(N)]

# Find optimal path
energy, path_length, path = find_optimal_path(N, K, plants)

# Output results
print(energy)
print(path_length)
for idx in path:
    print(plants[idx][0], plants[idx][1])
