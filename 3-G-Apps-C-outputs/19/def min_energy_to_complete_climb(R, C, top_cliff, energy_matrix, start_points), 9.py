
def min_energy_to_complete_climb(R, C, top_cliff, energy_matrix, start_points):
    INF = float('inf')
    dp = [[INF] * C for _ in range(R)]
    
    for r in range(R-1, -1, -1):
        for c in range(C):
            if r == R-1:
                dp[r][c] = max(0, -energy_matrix[r][c])
            else:
                dp[r][c] = max(0, -energy_matrix[r][c] + dp[r+1][c])
                if c > 0:
                    dp[r][c] = max(dp[r][c], max(0, -energy_matrix[r][c] + dp[r+1][c-1]))
                if c < C-1:
                    dp[r][c] = max(dp[r][c], max(0, -energy_matrix[r][c] + dp[r+1][c+1]))
    
    min_energy = INF
    for c in range(C):
        if top_cliff[c] == 'S':
            min_energy = min(min_energy, dp[0][c])
    
    return min_energy

# Input
R, C = map(int, input().split())
top_cliff = input().split()
energy_matrix = [list(map(int, input().split())) for _ in range(R)]
start_points = input().split()

# Output
print(min_energy_to_complete_climb(R, C, top_cliff, energy_matrix, start_points))
