
N = int(input())
A = [int(a) for a in input().split()]

ans = []
for i in range(N):
    if A[i] < 0:
        ans.append([N, i+1])
        A[N-1] += A[i]

print(len(ans))
for x, y in ans:
    print(x, y)
