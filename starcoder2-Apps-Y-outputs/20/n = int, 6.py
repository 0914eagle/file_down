
n = int(input())
h = list(map(int, input().split()))

ans = 0
for i in range(n):
    if h[i] < i:
        ans += i - h[i]
        h[i] = i
    if h[i] > i + 1:
        ans += h[i] - (i + 1)
        h[i] = i + 1
print(ans)

