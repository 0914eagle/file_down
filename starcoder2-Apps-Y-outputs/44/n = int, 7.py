
n = int(input())
a = list(map(int, input().split()))

ans = 1
for i in range(n - 1):
    if a[i + 1] <= a[i] * 2:
        ans += 1
    else:
        break
print(ans)

