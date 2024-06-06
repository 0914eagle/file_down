
n = int(input())
A, B = [], []
for i in range(n):
    a = list(map(int,input().split()))
    A.append(a)
for i in range(n):
    a = list(map(int,input().split()))
    B.append(a)
for i in range(1,n):
    if A[0][i-1] == 0 and A[1][i-1] == 0 and A[2][i-1] == 0 and A[3][i-1] == 0:
        print("Impossible")
        break
    if A[0][i-1] == 0 and A[1][i-1] == 0 and A[2][i-1] == 0 and A[3][i-1] == 0:
        print("Impossible")
        break
    if A[0][i-1] == 0 and A[1][i-1] == 0 and A[2][i-1] == 0 and A[3][i-1] == 0:
        print("Impossible")
        break
    if A[0][i-1] == 0 and A[1][i-1] == 0 and A[2][i-1] == 0 and A[3][i-1] == 0:
        print("Impossible")
        break
    if A[0][i-1] == 0 and A[1][i-1] == 0 and A[2][i-1] == 0 and A[3][i-1] == 0:
        print("Impossible")
        break
    if A[0][i-1] == 0 and A[1][i-1] == 0 and A[2][i-1] == 0 and A[3][i-1] == 0:
        print("Impossible")
        break
    if A[0][i-1] == 0 and A[1][i-1] == 0 and A[2][i-1] == 0 and A[3][i-1] == 0:
        print("Impossible")
        break
else:
    print("Yes")
