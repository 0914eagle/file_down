
def min_diff(N, W):
    W.sort()
    return min(abs(sum(W[:T]) - sum(W[T:])) for T in range(1, N))

N = int(input())
W = list(map(int, input().split()))
print(min_diff(N, W))

