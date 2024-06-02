
def max_messiness(n, k):
    if n == 1:
        return 0
    else:
        max_mess = n * (n - 1) // 2
        if k >= n // 2:
            return max_mess
        else:
            return 2 * k * (n - k)

# Read input
n, k = map(int, input().split())

# Call the function and print the output
print(max_messiness(n, k))
