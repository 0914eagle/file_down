
import sys

def solve_bug_fixing(B, T, f, bugs):
    dp = [[[0] * (T + 1) for _ in range(B + 1)] for _ in range(2)]

    for t in range(1, T + 1):
        for b in range(1, B + 1):
            p, s = bugs[b - 1]
            dp[0][b][t] = max(dp[0][b][t], dp[0][b][t - 1])
            dp[1][b][t] = max(dp[1][b][t], dp[1][b][t - 1])

            prob = p
            severity = s
            for prev_b in range(1, b):
                new_prob = p
                for i in range(1, t):
                    new_prob *= f
                    prob += new_prob * dp[0][prev_b][t - i - 1]
                    severity += new_prob * dp[1][prev_b][t - i - 1]

            dp[0][b][t] = max(dp[0][b][t], prob)
            dp[1][b][t] = max(dp[1][b][t], severity)

    return dp[1][B][T]

def main():
    B, T, f = map(float, input().strip().split())
    B, T = int(B), int(T)
    bugs = [list(map(float, input().strip().split())) for _ in range(B)]

    result = solve_bug_fixing(B, T, f, bugs)
    print("{:.6f}".format(result))

if __name__ == "__main__":
    main()
