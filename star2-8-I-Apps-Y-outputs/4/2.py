
N = int(input())
A = list(map(int, input().split()))
A.sort()
x = sum(A[:N//2])
y = sum(A[N//2:])
print(abs(x-y))

