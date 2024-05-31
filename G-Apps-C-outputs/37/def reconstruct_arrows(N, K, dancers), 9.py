
def reconstruct_arrows(N, K, dancers):
    arrows = [0] * N
    for i in range(N):
        arrows[dancers[i] - 1] = i + 1

    current = list(range(1, N + 1))
    for _ in range(K):
        next_positions = [current[arrows[i] - 1] for i in range(N)]
        current = next_positions

    if current == list(range(1, N + 1)):
        return arrows
    else:
        return "Impossible"

# Input processing
N, K = map(int, input().split())
dancers = list(map(int, input().split()))

# Call the function and print the result
result = reconstruct_arrows(N, K, dancers)
if result == "Impossible":
    print("Impossible")
else:
    print(*result)
