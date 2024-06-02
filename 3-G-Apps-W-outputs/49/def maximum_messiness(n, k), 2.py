
def maximum_messiness(n, k):
    if n == 1:
        return 0
    else:
        return n * (n - 1) // 2 * k

# Input
n, k = map(int, input().split())

# Output
print(maximum_messiness(n, k))
