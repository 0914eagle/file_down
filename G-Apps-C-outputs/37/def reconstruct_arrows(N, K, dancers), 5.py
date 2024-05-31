
def reconstruct_arrows(N, K, dancers):
    arrows = [0] * N
    for i in range(N):
        arrows[dancers[i] - 1] = i + 1
    
    # Check if it is possible to find a valid placement of arrows
    visited = [False] * N
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            current = i
            count = 1
            while arrows[current] != i + 1:
                current = arrows[current] - 1
                visited[current] = True
                count += 1
                if count > N:
                    print("Impossible")
                    return
    
    return arrows

# Read input
N, K = map(int, input().split())
dancers = list(map(int, input().split()))

# Reconstruct arrows
result = reconstruct_arrows(N, K, dancers)

# Print the result
if result:
    print(*result)
