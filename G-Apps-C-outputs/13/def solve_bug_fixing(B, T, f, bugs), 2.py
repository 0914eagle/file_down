
def solve_bug_fixing(B, T, f, bugs):
    dp = [[0] * (T + 1) for _ in range(B + 1)]
    
    # Sort bugs by severity in descending order
    bugs.sort(key=lambda x: x[1], reverse=True)
    
    for i in range(1, B + 1):
        p, s = bugs[i-1]
        for j in range(1, T + 1):
            dp[i][j] = max(dp[i][j], dp[i-1][j])
            prob = p
            severity = s
            for k in range(1, j+1):
                dp[i][j] = max(dp[i][j], dp[i-1][j-k] + prob * severity)
                prob *= f
                severity = max(0, severity - s)
    
    return dp[B][T]

# Input parsing
B, T, f = map(float, input().split())
B, T = int(B), int(T)
bugs = []
for _ in range(B):
    p, s = map(float, input().split())
    bugs.append((p, s))

result = solve_bug_fixing(B, T, f, bugs)
print("{:.6f}".format(result))
