
def reconstruct_arrows(N, K, positions):
    arrows = [0] * N
    for i in range(N):
        arrows[i] = positions.index(i+1) + 1
    return arrows

# Read input
N, K = map(int, input().split())
positions = list(map(int, input().split()))

# Reconstruct arrows
arrows = reconstruct_arrows(N, K, positions)

# Check if the reconstruction is valid
if len(set(arrows)) < N:
    print("Impossible")
else:
    print(*arrows)
