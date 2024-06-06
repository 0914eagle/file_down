
N = int(input())
ab = [input().split() for _ in range(2*N)]
A = [ab[i][1] for i in range(2*N) if ab[i][0] == "W"]
B = [ab[i][1] for i in range(2*N) if ab[i][0] == "B"]
cost = 0
for i in range(N-1):
    cost += min(A[i:].index(str(i+1)), B[i:].index(str(i+1)))
print(cost)
