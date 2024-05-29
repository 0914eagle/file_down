
def min_cuts(K, N, poles):
    max_length = max(poles)
    cuts = 0
    for pole in poles:
        cuts += (max_length - pole)
    return cuts

# Read input
K, N = map(int, input().split())
poles = list(map(int, input().split()))

# Output result
print(min_cuts(K, N, poles))
