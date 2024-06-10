
for t in range(int(input())):
    n = int(input())
    A = [0]*n
    B = [0]*n
    C = [0]*n
    for i in range(n):
        A[i], B[i], C[i] = map(int, input().split())
    maxApple = max(A)
    maxBanana = max(B)
    maxCarrot = max(C)
    count = 0
    for i in range(n):
        if A[i] >= maxApple and B[i] >= maxBanana and C[i] >= maxCarrot:
            count += 1
    print("Case #{}: {}".format(t+1, count))

