
n = int(input())
a = list(map(int, input().split()))
a.sort()
i = 0
ans = 0
while i < n:
    cnt = 0
    while i < n and a[i] >= ans + 1:
        i += 1
        cnt += 1
    ans += cnt
    i += 1
print(ans)

