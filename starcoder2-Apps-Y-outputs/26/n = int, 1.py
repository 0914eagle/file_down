
n = int(input())
a = list(map(int, input().split()))
b = [0] * (n + 1)
for i in range(n):
    if a[i] == 0:
        for j in range(1, n + 1):
            if b[j] == 0:
                a[i] = j
                b[j] = 1
                break
print(*a)

