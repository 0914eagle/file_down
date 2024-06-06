
n = int(input())
W = []
for i in range(n):
    W.append(list(map(int, input().split())))

A = [[0 for i in range(n)] for j in range(n)]
B = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(i, n):
        A[i][j] = (W[i][j] + W[j][i]) / 2
        A[j][i] = A[i][j]
        B[i][j] = (W[i][j] - W[j][i]) / 2
        B[j][i] = -B[i][j]

for i in range(n):
    for j in range(n):
        print(A[i][j], end=" ")
    print()
for i in range(n):
    for j in range(n):
        print(B[i][j], end=" ")
    print()
