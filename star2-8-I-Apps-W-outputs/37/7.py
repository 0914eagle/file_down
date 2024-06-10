
n, h = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    if a[i] <= h:
        ans += 1
    else:
        ans += 2
print(ans)

