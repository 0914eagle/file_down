
def min_diff(N, W):
    # Write your code here
    W.sort()
    return abs(sum(W[:2]) - sum(W[2:]))

