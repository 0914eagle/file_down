
A, B, K = map(int, input().split())

for _ in range(K):
    if A > 0:
        A -= 1
    elif B > 0:
        B -= 1

print(A, B)

