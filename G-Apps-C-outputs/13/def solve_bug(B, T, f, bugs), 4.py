
def solve_bug(B, T, f, bugs):
    dp = [[0.0 for _ in range(T+1)] for _ in range(B+1)]
    
    for t in range(1, T+1):
        for b in range(1, B+1):
            p, s = bugs[b-1]
            dp[b][t] = max(dp[b][t], dp[b][t-1])  # Skip working on this bug
            
            prob = p
            total_severity = s
            for i in range(1, t):
                prob *= f
                total_severity += s * (1 - prob)
                dp[b][t] = max(dp[b][t], dp[b-1][t-i] + total_severity)
    
    return dp[B][T]

# Input reading
B, T, f = map(float, input().split())
B = int(B)
T = int(T)
f = float(f)
bugs = []
for _ in range(B):
    p, s = map(float, input().split())
    bugs.append((p, s))

result = solve_bug(B, T, f, bugs)
print('%.6f' % result)
