

def solve(N, K, d, A):
    # Write your code here
    snack = [0] * K
    for i in range(N):
        for j in range(d[i]):
            snack[A[i][j] - 1] += 1
    return sum(snack)

N, K = map(int, input().split())
d = [int(input()) for _ in range(N)]
A = [[int(i) for i in input().split()] for _ in range(N)]
print(solve(N, K, d, A))

