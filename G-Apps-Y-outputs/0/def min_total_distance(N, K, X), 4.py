
def min_total_distance(N, K, X):
    min_distance = float('inf')
    for i in range(N):
        for j in range(N):
            distance = max(abs(X[j] - X[i]), abs(X[j] - K) + abs(X[i]))
            min_distance = min(min_distance, distance)
    return min_distance

# Input
N = int(input())
K = int(input())
X = list(map(int, input().split()))

# Call the function and print the result
print(min_total_distance(N, K, X))
