
import sys

def check_bingo(A, N, B):
    # check rows
    for i in range(3):
        if sum(A[i][j] in B for j in range(3)) == 3:
            return True

    # check cols
    for j in range(3):
        if sum(A[i][j] in B for i in range(3)) == 3:
            return True

    # check diagonals
    if sum(A[i][i] in B for i in range(3)) == 3:
        return True

    if sum(A[i][2 - i] in B for i in range(3)) == 3:
        return True

    return False

if __name__ == '__main__':
    A = []
    for i in range(3):
        A.append(list(map(int, sys.stdin.readline().split())))

    N = int(sys.stdin.readline())
    B = list(map(int, sys.stdin.readline().split()))

    if check_bingo(A, N, B):
        print("Yes")
    else:
        print("No")

