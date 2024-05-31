
def min_total_distance(N, K, x):
    total_distance = 0
    for xi in x:
        total_distance += min(xi, K - xi) * 2
    return total_distance

# Read input
N = int(input())
K = int(input())
x = list(map(int, input().split()))

# Call the function and print the result
print(min_total_distance(N, K, x))
