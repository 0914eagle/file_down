
def max_messiness(n, k):
    if n == 1:
        return 0
    total_pairs = n * (n - 1) // 2
    if k >= n // 2:
        return total_pairs
    else:
        return 2 * k * (n - k)

# Input processing
n, k = map(int, input().split())

# Output
print(max_messiness(n, k))
