
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

acc1 = [0] * (N + 1)
acc2 = [0] * (N + 1)

for i in range(N):
    acc1[i + 1] = acc1[i] + abs(A[i] - 0)
    acc2[i + 1] = acc2[i] + abs(A[N - i - 1] - 0)

for i in range(N):
    print(acc1[i] + acc2[N - i - 1] - abs(A[i] - 0))

