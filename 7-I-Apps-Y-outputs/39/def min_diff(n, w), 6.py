
def min_diff(n, w):
    w.sort()
    return min(abs(w[i]-w[n-i-1]) for i in range(n//2))

