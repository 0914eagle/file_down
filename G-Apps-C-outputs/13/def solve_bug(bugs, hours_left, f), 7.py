
import sys

def solve_bug(bugs, hours_left, f):
    b = len(bugs)
    dp = [[0] * (hours_left + 1) for _ in range(b + 1)]

    for i in range(1, b + 1):
        for j in range(1, hours_left + 1):
            p, s = bugs[i-1]
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + p * s)

            for k in range(1, j):
                dp[i][j] = max(dp[i][j], dp[i-1][k-1] + p * (1 - f**(j-k)) * s)

    return dp[b][hours_left]

# Read input
B, T, f = map(float, input().split())
B = int(B)
T = int(T)
f = float(f)

bugs = []
for _ in range(B):
    p, s = map(float, input().split())
    bugs.append((p, s))

# Output the result with 6 decimal places
result = solve_bug(bugs, T, f)
print('{:.6f}'.format(result))
