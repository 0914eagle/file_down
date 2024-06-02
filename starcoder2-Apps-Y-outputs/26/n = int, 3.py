
n = int(input())
f = list(map(int, input().split()))

ans = [0] * n
for i in range(n):
    if f[i] == 0:
        for j in range(n):
            if ans[j] == 0:
                ans[j] = i + 1
                break

for i in range(n):
    if ans[i] == 0:
        ans[i] = f[i]

print(*ans)

