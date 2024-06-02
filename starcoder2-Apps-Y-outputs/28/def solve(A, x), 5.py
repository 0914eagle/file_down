
N, x = map(int, input().split())
A = list(map(int, input().split()))

def solve(A, x):
    ans = 0
    for i in range(1, N):
        if A[i] + A[i-1] > x:
            ans += A[i] + A[i-1] - x
            A[i] = x - A[i-1]
    return ans

print(solve(A, x))

