
n, d = map(int, input().split())
apples = [0] * n
apples[0] = 1
inspectors = [0] * n

for i in range(n):
    if apples[i]:
        for j in range(max(0, i - d), min(n, i + d + 1)):
            inspectors[j] = 1
print(inspectors.count(1))

