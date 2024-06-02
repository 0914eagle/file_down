
n = int(input())
f = [int(x) for x in input().split()]

for i in range(n):
    if f[i] == 0:
        for j in range(n):
            if j != i and f[j] != 0 and f[j] != i:
                f[i] = j
                break

print(*f)

