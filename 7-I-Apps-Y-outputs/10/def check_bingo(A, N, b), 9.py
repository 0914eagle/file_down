

def check_bingo(A, N, b):
    # TODO: Write your code here
    for i in range(3):
        for j in range(3):
            if A[i][j] in b:
                b.remove(A[i][j])
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


if __name__ == "__main__":
    main()

