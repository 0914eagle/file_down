
n, s, m, k = map(int, input().split())
arr = list(map(int, input().split()))
seg = []
for i in range(s):
    l, r = map(int, input().split())
    seg.append((l, r))

seg.sort()
arr.sort()

dp = [[0] * (n + 1) for i in range(m + 1)]
dp[0][0] = 1
for i in range(s):
    for j in range(m + 1):
        for l in range(n, -1, -1):
            if dp[j][l]:
                for k in range(seg[i][0] - 1, seg[i][1]):
                    dp[j + 1][k] = 1

ans = -1
for i in range(n + 1):
    if dp[m][i]:
        ans = max(ans, arr[i])

print(ans)
