
def min_diff(N, W):
    W.sort()
    return min(abs(sum(W[:T]) - sum(W[T:])), abs(sum(W[:T+1]) - sum(W[T+1:])))

N = int(input())
W = list(map(int, input().split()))
print(min_diff(N, W))

