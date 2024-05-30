
import sys

def main():
    # Read the first 9 lines of input.
    A = []
    for i in range(3):
        A.append(list(map(int, sys.stdin.readline().split())))

    # Read the number of numbers to choose.
    N = int(sys.stdin.readline())

    # Read the numbers to choose.
    b = list(map(int, sys.stdin.readline().split()))

    # Check if we will have a bingo.
    for i in range(3):
        # Check if we have three numbers in a row.
        if b[0] in A[i] and b[1] in A[i] and b[2] in A[i]:
            print("Yes")
            return

        # Check if we have three numbers in a column.
        if b[0] in A[:, i] and b[1] in A[:, i] and b[2] in A[:, i]:
            print("Yes")
            return

    # Check if we have three numbers in the diagonal.
    if b[0] in A[0, 0:3] and b[1] in A[1, 1:4] and b[2] in A[2, 2:5]:
        print("Yes")
        return

    # Check if we have three numbers in the anti-diagonal.
    if b[0] in A[2, 0:3] and b[1] in A[1, 1:4] and b[2] in A[0, 2:5]:
        print("Yes")
        return

    print("No")

main()

