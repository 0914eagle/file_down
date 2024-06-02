
n = int(input())
a = list(map(int, input().split()))

ans = [0] * n

for i in range(n):
    if a[i] == 0:
        ans[i] = i + 1
    else:
        ans[i] = a[i]

for i in range(n):
    if ans[i] == 0:
        ans[i] = ans[a[i] - 1]

print(*ans)

