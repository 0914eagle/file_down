
n = int(input())
a = list(map(int, input().split()))

ans = 1

for i in range(1, n):
    if a[i] <= 2 * a[i - 1]:
        ans += 1
    else:
        break

print(ans)

