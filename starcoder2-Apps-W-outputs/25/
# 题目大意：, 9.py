
# 题目大意：给定一个n*n的矩阵，要求构造两个n*n的矩阵A和B，使得A+B=W，且A为对称矩阵，B为反对称矩阵
# 思路：A=W+B，B=W-A，所以只需要构造一个对称矩阵B，然后A=W+B，B=W-A即可
# 注意：题目中要求输出的小数点后保留8位小数，所以在计算的时候，需要将整数转换为浮点数，否则会出现精度问题

n = int(input())
W = []
for i in range(n):
    W.append(list(map(int, input().split())))

B = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        B[i][j] = (W[i][j] - W[j][i]) / 2.0
        B[j][i] = -B[i][j]

A = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        A[i][j] = W[i][j] - B[i][j]

for i in range(n):
    for j in range(n):
        print(A[i][j], end=' ')
    print()
for i in range(n):
    for j in range(n):
        print(B[i][j], end=' ')
    print()
