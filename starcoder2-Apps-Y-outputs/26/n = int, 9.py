
n = int(input())
f = list(map(int, input().split()))

ans = [0] * n

for i in range(n):
    if f[i] == 0:
        ans[i] = i + 1
    else:
        ans[i] = f[i]

for i in range(n):
    if ans[i] == 0:
        ans[i] = i + 1

for i in range(n):
    print(ans[i], end=' ')

