
def reconstruct_arrows(N, K, dancers):
    arrows = [0] * N
    for i in range(N):
        arrows[dancers[i] - 1] = i + 1
    return arrows

# Input processing
N, K = map(int, input().split())
dancers = list(map(int, input().split()))

# Reconstruct arrows and check if it's possible
arrows = reconstruct_arrows(N, K, dancers)
if arrows.count(0) == 1:
    remaining_idx = arrows.index(0)
    for i in range(N):
        if arrows[i] == 0:
            arrows[i] = remaining_idx + 1
    print(*arrows)
else:
    print("Impossible")
