
n, m = map(int, input().split())
ans = 0
for i in range(1, n+1):
    if m % i == 0:
        ans += 1
print(ans % (10**9 + 7))

