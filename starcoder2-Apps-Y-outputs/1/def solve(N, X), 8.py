

def solve(N, X):
    X.sort()
    for i in range(N):
        if i == 0:
            print(X[N // 2])
        elif i == N - 1:
            print(X[N // 2 - 1])
        else:
            if i % 2 == 0:
                print(X[N // 2 - 1])
            else:
                print(X[N // 2])

N = int(input())
X = list(map(int, input().split()))
solve(N, X)


