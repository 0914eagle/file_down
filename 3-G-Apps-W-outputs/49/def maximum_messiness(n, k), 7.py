
def maximum_messiness(n, k):
    if n == 1:
        return 0
    else:
        return n * (n - 1) // 2 * k

# Read input
n, k = map(int, input().split())

# Calculate and print the maximum messiness
print(maximum_messiness(n, k))
