
t = int(input())
a = list(map(int, input().split()))

def find_matrix(a):
    n = len(a)
    for i in range(1, n+1):
        if n % i == 0:
            m = n // i
            if check_matrix(a, i, m):
                return i, m
    return -1, -1

def check_matrix(a, n, m):
    matrix = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            matrix[i][j] = a.pop(0)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 0:
                if abs(i - n // 2) + abs(j - m // 2) != matrix[i][j]:
                    return False
    return True

n, m = find_matrix(a)
if n == -1:
    print(-1)
else:
    print(n, m)
    print(n // 2 + 1, m // 2 + 1)

