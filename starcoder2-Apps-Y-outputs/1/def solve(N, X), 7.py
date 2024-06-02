
def solve(N, X):
    X.sort()
    for i in range(N):
        if i < N // 2:
            print(X[N // 2])
        else:
            print(X[N // 2 - 1])

N = int(input())
X = list(map(int, input().split()))
solve(N, X)

