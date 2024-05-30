
def min_diff(N, W):
    # Write your code here
    if N == 1:
        return 0
    if N == 2:
        return abs(W[0] - W[1])
    if N == 3:
        return min(abs(W[0] - W[1]), abs(W[0] - W[2]), abs(W[1] - W[2]))
    min_diff = float('inf')
    for i in range(1, N):
        min_diff = min(min_diff, abs(sum(W[:i]) - sum(W[i:])))
    return min_diff


if __name__ == '__main__':
    N = int(input())
    W = list(map(int, input().split()))
    print(min_diff(N, W))

