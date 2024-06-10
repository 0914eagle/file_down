
n, k_1, k_2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
while k_1 > 0 or k_2 > 0:
    if A[0] < B[0]:
        if k_1 > 0:
            A[0] += 1
            k_1 -= 1
        else:
            B[0] -= 1
            k_2 -= 1
    else:
        if k_2 > 0:
            B[0] += 1
            k_2 -= 1
        else:
            A[0] -= 1
            k_1 -= 1
print(sum([(A[i] - B[i])**2 for i in range(n)]))

