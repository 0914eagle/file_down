
n, d = map(int, input().split())
inspectors = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(max(i - d, 1), min(i + d + 1, n + 1)):
        inspectors[j] = 1
print(sum(inspectors))

