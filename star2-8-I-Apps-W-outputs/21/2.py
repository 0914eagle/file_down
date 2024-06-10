
n = int(input())
p = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += (1 - p[i] / 100)
print(int(ans) % 998244353)

