
def reconstruct_arrows(N, K, dancers):
    arrows = [-1] * N
    for i in range(N):
        arrows[dancers[i] - 1] = i + 1

    for _ in range(K):
        new_arrows = [-1] * N
        for i in range(N):
            if arrows[i] != -1:
                new_arrows[arrows[i] - 1] = dancers[i]

        arrows = new_arrows

    if -1 in arrows:
        print("Impossible")
    else:
        print(*arrows)

# Read input
N, K = map(int, input().split())
dancers = list(map(int, input().split()))

# Call the function with the input data
reconstruct_arrows(N, K, dancers)
