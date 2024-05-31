
def reconstruct_arrows(N, K, dancers):
    arrows = [0] * N
    for i in range(N):
        arrows[dancers[i] - 1] = i + 1
    
    for _ in range(K % 2):
        new_arrows = [0] * N
        for i in range(N):
            new_arrows[i] = arrows[dancers[i] - 1]
        arrows = new_arrows

    if arrows == list(range(1, N+1)):
        return arrows
    else:
        return "Impossible"

# Read input
N, K = map(int, input().split())
dancers = list(map(int, input().split()))

# Call the function and print the output
result = reconstruct_arrows(N, K, dancers)
if result == "Impossible":
    print("Impossible")
else:
    print(*result)
