
A, B, K = map(int, input().split())

for i in range(A, B+1):
    if i in range(A, A+K) or i in range(B-K+1, B+1):
        print(i)

