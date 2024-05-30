
def check_bingo(A, N, b):
    # Your code goes here
    for i in range(3):
        for j in range(3):
            if A[i][j] in b:
                b.remove(A[i][j])
    for i in range(3):
        for j in range(3):
            if A[j][i] in b:
                b.remove(A[j][i])
    for i in range(3):
        if A[i][0] in b and A[i][1] in b and A[i][2] in b:
            b.remove(A[i][0])
            b.remove(A[i][1])
            b.remove(A[i][2])
    if len(b) == 0:
        return True
    else:
        return False

def main():
    A = []
    for i in range(3):
        A.append(list(map(int, input().split())))
    N = int(input())
    b = list(map(int, input().split()))
    if check_bingo(A, N, b):
        print("Yes")
    else:
        print("No")

main()

