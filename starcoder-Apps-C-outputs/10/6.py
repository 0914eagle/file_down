
def solve():
    n, m = map(int, input().split())
    dp = [[] for _ in range(n)]
    id = 0
    for _ in range(n):
        x = list(map(int, input().split()))
        if x[1] > id:
            id = x[1]
            dp[0] = x
        if x[2] > dp[0][2]:
            dp[0] = x
    dp[1] = [0] * 3
    for _ in range(m):
        x = int(input())
        if x == dp[0][0]:
            print('0 0')
        for i in range(n):
            if dp[i][1] == x:
                print(dp[i+1][0], len(dp)-i-1)
        for i in range(n):
            if dp[i][0] == x:
                if i == 0:
                    dp[1] = dp[i]
                else:
                    dp[i] = dp[i-1]

if __name__ == '__main__':
    solve()
