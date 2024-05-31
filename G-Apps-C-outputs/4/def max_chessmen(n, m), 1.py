
def max_chessmen(n, m):
    if n < 2 or m < 2:  # Not enough space for chessmen
        return 0
    elif n == 2 and m == 2:  # Special case
        return 0
    else:
        return (n // 2) * m * 2

# Read input
n, m = map(int, input().split())

# Calculate and print the result
print(max_chessmen(n, m))
