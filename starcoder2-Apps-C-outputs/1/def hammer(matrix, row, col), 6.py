
# 思路：
# 1. 先把两个矩阵存起来
# 2. 遍历第一个矩阵，如果是X，则跳过，如果是O，则把它周围的O变成X
# 3. 遍历第二个矩阵，如果是X，则跳过，如果是O，则把它周围的O变成X
# 4. 最后比较两个矩阵，如果相同，则返回1，否则返回0

import sys

def hammer(matrix, row, col):
    matrix[row][col] = 'X'
    if row - 1 >= 0:
        matrix[row - 1][col] = 'X'
    if row + 1 < len(matrix):
        matrix[row + 1][col] = 'X'
    if col - 1 >= 0:
        matrix[row][col - 1] = 'X'
    if col + 1 < len(matrix[0]):
        matrix[row][col + 1] = 'X'

def judge(matrix1, matrix2):
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            if matrix1[i][j] == 'O':
                hammer(matrix1, i, j)
    for i in range(len(matrix2)):
        for j in range(len(matrix2[0])):
            if matrix2[i][j] == 'O':
                hammer(matrix2, i, j)
    return matrix1 == matrix2

if __name__ == '__main__':
    while True:
        try:
            row, col = map(int, sys.stdin.readline().strip().split())
            matrix1 = []
            matrix2 = []
            for i in range(row):
                matrix1.append(list(sys.stdin.readline().strip()))
            for i in range(row):
                matrix2.append(list(sys.stdin.readline().strip()))
            if judge(matrix1, matrix2):
                print(1)
            else:
                print(0)
        except:
            break
