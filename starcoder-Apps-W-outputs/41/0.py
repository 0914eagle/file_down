
n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
for i in range(1, 101):
    cnt = 0
    for j in range(m):
        if a[j] == i:
            cnt += 1
    if cnt >= n:
        ans = max(ans, cnt // n)
print(ans)
