
n, d = map(int, input().split())
apples = [0] * n

for i in range(n):
    if i - d >= 0:
        apples[i - d] += 1
    if i + d < n:
        apples[i + d] += 1

print(max(apples))

