
[CODE]
n, k = map(int, input().split())
a = list(map(int, input().split()))
ways = [0] * (k + 1)
ways[0] = 1
for i in range(n):
    for j in range(k, a[i] - 1, -1):
        ways[j] += ways[j - a[i]]
print(-1 if ways[k] == 0 else ways[k])
[/CODE]

