
n, x, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    cnt = 0
    for j in range(i, n):
        if a[i] <= a[j]:
            cnt += 1
            if cnt == k + 1 and ((a[j] - a[i]) % x == 0):
                ans += 1
print(ans)
