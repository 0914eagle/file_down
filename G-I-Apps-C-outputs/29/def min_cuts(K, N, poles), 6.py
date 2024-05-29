
def min_cuts(K, N, poles):
    max_len = max(poles)
    cuts = 0
    for pole in poles:
        if pole < max_len:
            cuts += 1
    return cuts

# Reading input
K, N = map(int, input().split())
poles = list(map(int, input().split()))

# Output
print(min_cuts(K, N, poles))
