
def solve(N, W):
    # Write your code here
    W.sort()
    return abs(sum(W[:N//2]) - sum(W[N//2:]))
