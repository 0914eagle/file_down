
n = int(input())
m = [[int(i) for i in input().split()] for j in range(n)]

# Двумерный список для матрицы
matrix = []

# Ввод элементов матрицы
for i in range(n):
    a = []
    for j in range(n):
        a.append(int(input()))
    matrix.append(a)

print("Исходная матрица:")
for row in matrix:
    for elem in row:
        print(elem, end=' ')
    print()
