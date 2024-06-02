
def min_energy_to_complete_climb(R, C, cliff_top, cliff_energy, start_points):
    dp = [[float('inf')] * C for _ in range(R)]
    
    for r in range(R):
        for c in range(C):
            dp[r][c] = cliff_energy[r][c]
            if r > 0:
                dp[r][c] = min(dp[r][c], dp[r-1][c] + cliff_energy[r][c])
            if c > 0:
                dp[r][c] = min(dp[r][c], dp[r][c-1] + cliff_energy[r][c])
    
    min_energy = float('inf')
    for start_point in start_points:
        r, c = start_point
        min_energy = min(min_energy, dp[r][c])
    
    return min_energy

# Input parsing
R, C = map(int, input().split())
cliff_top = input().split()
cliff_energy = []
for _ in range(R):
    cliff_energy.append(list(map(int, input().split())))
start_points = []
for r in range(R):
    for c in range(C):
        if cliff_top[c] == 'S':
            start_points.append((r, c))

# Call the function and print the result
print(min_energy_to_complete_climb(R, C, cliff_top, cliff_energy, start_points))
