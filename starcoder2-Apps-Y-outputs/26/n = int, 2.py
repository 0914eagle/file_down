
n = int(input())
f = list(map(int, input().split()))

for i in range(n):
    if f[i] == 0:
        for j in range(n):
            if j != i and j not in f:
                f[i] = j + 1
                break

print(*f)

