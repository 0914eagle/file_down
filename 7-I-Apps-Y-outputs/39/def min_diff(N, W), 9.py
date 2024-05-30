
def min_diff(N, W):
    W.sort()
    S1 = sum(W[:N//2])
    S2 = sum(W[N//2:])
    return abs(S1 - S2)

