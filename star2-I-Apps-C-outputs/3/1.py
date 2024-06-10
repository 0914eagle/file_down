
import sys
def main():
    d, g, n, k = map(int, sys.stdin.readline().split())
    dp = [[0 for _ in range(d+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, d+1):
            if i <= k:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
            else:
                for bet in range(1, min(j, g)+1):
                    dp[i][j] = max(dp[i][j], bet + dp[i-1][j-bet])
    print(dp[n][d])
if __name__ == "__main__":
    main()

