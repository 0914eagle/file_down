
def solve(N, K, H):
    H.sort() # Sort the list in ascending order
    min_diff = 10**9 + 7 # Initialize the minimum difference with a large value
    for i in range(N - K + 1):
        diff = H[i + K - 1] - H[i] # Calculate the difference between the tallest and shortest trees
        if diff < min_diff:
            min_diff = diff # Update the minimum difference if necessary
    return min_diff

N, K = map(int, input().split())
H = [int(input()) for _ in range(N)]
print(solve(N, K, H))

