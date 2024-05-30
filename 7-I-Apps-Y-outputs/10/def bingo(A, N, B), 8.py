
def bingo(A, N, B):
    # Fill this in.
    for i in range(len(B)):
        for j in range(len(A)):
            for k in range(len(A[0])):
                if A[i][j] == B[k]:
                    A[i][j] = "*"
                    break
    for i in range(len(A)):
        if "*" in A[i]:
            continue
        else:
            return False
    for j in range(len(A[0])):
        if "*" in [A[i][j] for i in range(len(A))]:
            continue
        else:
            return False
    if "*" in [A[i][i] for i in range(len(A))]:
        return True
    else:
        return False


if __name__ == "__main__":
    A = []
    for _ in range(3):
        A.append(list(map(int, input().split())))
    N = int(input())
    B = list(map(int, input().split()))
    if bingo(A, N, B):
        print("Yes")
    else:
        print("No")

