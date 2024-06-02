
def min_energy_to_complete_climb(R, C, top_cliff, cliff_energy, start_points):
    dp = [[float('inf')] * C for _ in range(R)]
    
    for r in range(R-1, -1, -1):
        for c in range(C):
            if r == R-1:
                dp[r][c] = max(0, -cliff_energy[r][c])
            else:
                dp[r][c] = max(0, -cliff_energy[r][c] + dp[r+1][c])
                if c > 0:
                    dp[r][c] = max(dp[r][c], max(0, -cliff_energy[r][c] + dp[r+1][c-1]))
                if c < C-1:
                    dp[r][c] = max(dp[r][c], max(0, -cliff_energy[r][c] + dp[r+1][c+1]))
    
    min_energy = float('inf')
    for c in range(C):
        if top_cliff[c] == 'S':
            min_energy = min(min_energy, dp[0][c])
    
    return min_energy

# Input parsing
R, C = map(int, input().split())
top_cliff = input().split()
cliff_energy = []
for _ in range(R):
    cliff_energy.append(list(map(int, input().split())))
start_points = input().split()

# Call the function and output the result
print(min_energy_to_complete_climb(R, C, top_cliff, cliff_energy, start_points))
