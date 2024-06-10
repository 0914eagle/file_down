
n, k = map(int, input().split())
h = list(map(int, input().split()))

ans = 0
for a in range(1, k+1):
    prev = a
    cnt = 0
    for i in range(n):
        if prev == h[i]:
            cnt += 1
        prev = (prev % n) + 1
    if cnt > 0:
        ans += k ** (n - cnt) * (k - 1) ** cnt

print(ans % 998244353)

