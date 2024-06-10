
def solve(S):
    dp = [[0] * 10 for _ in range(S + 1)]
    dp[0][0] = 1
    for s in range(1, S + 1):
        for d in range(1, 10):
            for i in range(10):
                dp[s][d] += dp[s - 1][i]
    return sum(dp[S]) % (10**9 + 7)

if __name__ == '__main__':
    S = int(input())
    print(solve(S))

