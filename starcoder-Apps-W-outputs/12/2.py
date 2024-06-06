
n, t, c = map(int, input().split())
a = list(map(int, input().split()))

k = 0
for i in range(n):
    if a[i] > t:
        break
    k += 1
ans = 0

for i in range(n - k):
    if a[i] <= t and a[i + k - 1] <= t:
        ans += 1
print(ans)
