
n = int(input())

x = [0 for i in range(101)]
y = [0 for i in range(101)]

for i in range(n):
    a, b = map(int, input().split())
    x[a] += 1
    y[b] += 1

ans = 0
for i in range(101):
    ans += min(x[i], y[i])

print(ans)
