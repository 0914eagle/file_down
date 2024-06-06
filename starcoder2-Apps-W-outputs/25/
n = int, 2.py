
n = int(input())
w = []
for i in range(n):
    w.append(list(map(int, input().split())))

a = [[0 for i in range(n)] for j in range(n)]
b = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(i+1, n):
        a[i][j] = (w[i][j] + w[j][i]) / 2
        a[j][i] = a[i][j]
        b[i][j] = (w[i][j] - w[j][i]) / 2
        b[j][i] = -b[i][j]

for i in range(n):
    print(*a[i])
for i in range(n):
    print(*b[i])
