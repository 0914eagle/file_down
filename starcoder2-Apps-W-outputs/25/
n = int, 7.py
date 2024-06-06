
n = int(input())
w = []
for i in range(n):
    w.append(list(map(int, input().split())))

a = [[0 for i in range(n)] for j in range(n)]
b = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(i, n):
        if i == j:
            a[i][j] = w[i][j]
        else:
            a[i][j] = (w[i][j] + w[j][i]) / 2
            b[i][j] = (w[i][j] - w[j][i]) / 2
            b[j][i] = -b[i][j]

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
for i in range(n):
    for j in range(n):
        print(b[i][j], end=' ')
    print()
