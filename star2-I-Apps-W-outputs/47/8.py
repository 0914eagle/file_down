
from sys import stdin
input = stdin.readline

def main():
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    foe = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        foe[a].append(b)
        foe[b].append(a)
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        dp[i] = dp[i-1] * 2
        for j in foe[p[i-1]]:
            if j < p[i-1]:
                continue
            dp[i] -= dp[j-1]
    print(dp[n])

if __name__ == '__main__':
    main()

