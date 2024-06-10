
n, k1, k2 = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
for i in range(k1):
    A[i] += 1
for i in range(k2):
    B[i] += 1
error = 0
for i in range(n):
    error += (A[i] - B[i])**2
print(error)

