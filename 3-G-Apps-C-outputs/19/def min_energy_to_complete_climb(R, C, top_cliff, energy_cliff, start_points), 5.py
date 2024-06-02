
def min_energy_to_complete_climb(R, C, top_cliff, energy_cliff, start_points):
    dp = [[float('inf')] * C for _ in range(R)]
    
    for r in range(R):
        for c in range(C):
            dp[r][c] = energy_cliff[r][c]
            if r > 0:
                dp[r][c] = min(dp[r][c], dp[r-1][c] + energy_cliff[r][c])
            if c > 0:
                dp[r][c] = min(dp[r][c], dp[r][c-1] + energy_cliff[r][c])
    
    min_energy = float('inf')
    for start_point in start_points:
        r, c = start_point
        min_energy = min(min_energy, dp[r][c])
    
    return min_energy

# Input parsing
R, C = map(int, input().split())
top_cliff = input().split()
energy_cliff = [list(map(int, input().split())) for _ in range(R)]
start_points = [(r, c) for r in range(R) for c in range(C) if top_cliff[c] == 'S']

# Call the function and print the result
print(min_energy_to_complete_climb(R, C, top_cliff, energy_cliff, start_points))
