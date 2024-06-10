
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
ans = 0
i = 0
for x in b:
    while i < n and a[i] + x < 2:
        i += 1
    if i < n and a[i] + x == 2:
        ans += 1
        i += 1
print(ans)

