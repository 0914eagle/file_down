
def main():
    n,k = map(int,input().split())
    s = input()
    a = [int(input()) for i in range(n)]
    dp = [[float('inf')]*(k+1) for i in range(n+1)]
    dp[0][0] = 0
    for i in range(1,n+1):
        for j in range(k+1):
            if j>0:
                dp[i][j] = min(dp[i-1][j-1]+a[i-1],dp[i-1][j],dp[i][j-1])
            else:
                dp[i][j] = min(dp[i-1][j]+a[i-1],dp[i-1][j],dp[i][j])
    if dp[n][k] < float('inf'):
        print(dp[n][k])
    else:
        print('?')

if __name__=='__main__':
    main()
