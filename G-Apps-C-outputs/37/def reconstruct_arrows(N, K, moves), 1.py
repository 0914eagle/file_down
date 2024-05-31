
def reconstruct_arrows(N, K, moves):
    arrows = [0] * N
    for i in range(N):
        arrows[i] = moves[i] - 1

    for _ in range(K):
        new_arrows = [0] * N
        for i in range(N):
            new_arrows[i] = arrows[arrows[i]]
        arrows = new_arrows

    if arrows == list(range(N)):
        return arrows
    else:
        return "Impossible"

# Input parsing
N, K = map(int, input().split())
moves = list(map(int, input().split()))

result = reconstruct_arrows(N, K, moves)
if result == "Impossible":
    print(result)
else:
    print(" ".join(map(str, result)))
