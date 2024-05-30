
def check_bingo(A, N, B):
    # Write your code here
    for i in range(3):
        for j in range(3):
            if A[i][j] in B:
                B.remove(A[i][j])
    if len(B) == 0:
        return True
    return False


def main():
    A = []
    N = int(input())
    for i in range(3):
        A.append(list(map(int, input().split())))
    B = list(map(int, input().split()))
    if check_bingo(A, N, B):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

