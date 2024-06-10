
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
i, j = 0, 0
while i < n and j < m:
    if (a[i] + b[j]) % 2 == 1:
        ans += 1
        i += 1
        j += 1
    else:
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
print(ans)

