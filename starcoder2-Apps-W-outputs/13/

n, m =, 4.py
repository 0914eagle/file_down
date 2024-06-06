

n, m = map(int, input().split())

x = [0] * (n + 1)
y = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    x[a] += 1
    y[b] += 1

ans = n * n
for i in range(1, n + 1):
    ans -= x[i] * y[i]
    print(ans, end=" ")

