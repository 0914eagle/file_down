
def min_total_distance(N, K, x):
    min_distance = 0
    for xi in x:
        min_distance += min(xi*2, (K-xi)*2)
    return min_distance

# Read input
N = int(input())
K = int(input())
x = list(map(int, input().split()))

# Call the function and print the result
print(min_total_distance(N, K, x))
