
def parenthesization_game():
    n, k = map(int, input().strip().split())
    s = input().strip()
    c = [int(input().strip()) for i in range(n)]
    dp = [[0 for i in range(k + 1)] for j in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(k + 1):
            if s[i] == '(':
                dp[i][j] = 1000000000
            else:
                if j == 0:
                    dp[i][j] = 1000000000
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i + 1][j - 1] + c[i])
    ans = min(dp[0])
    if ans >= 1000000000:
        print('?')
    else:
        print(ans)
parenthesization_game()
