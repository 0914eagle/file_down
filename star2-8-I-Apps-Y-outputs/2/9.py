
N = int(input())
A = list(map(int, input().split()))
A.sort()
print(min([A[i + 1] - A[i] for i in range(N - 1)]))

