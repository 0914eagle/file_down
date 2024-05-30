
import sys

def bingo(A, N, b):
    # Write your code here
    for i in range(3):
        for j in range(3):
            if A[i][j] in b:
                b.remove(A[i][j])
        if len(b) == 0:
            return 'Yes'
    for i in range(3):
        for j in range(3):
            if A[j][i] in b:
                b.remove(A[j][i])
        if len(b) == 0:
            return 'Yes'
    for i in range(3):
        if A[i][i] in b:
            b.remove(A[i][i])
        if len(b) == 0:
            return 'Yes'
    for i in range(3):
        if A[i][2-i] in b:
            b.remove(A[i][2-i])
        if len(b) == 0:
            return 'Yes'
    return 'No'

if __name__ == '__main__':
    A = []
    N = int(input())
    for i in range(3):
        A.append(list(map(int, input().split())))
    b = list(map(int, input().split()))
    print(bingo(A, N, b))

