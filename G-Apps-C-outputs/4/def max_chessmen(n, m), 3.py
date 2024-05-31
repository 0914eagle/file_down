
def max_chessmen(n, m):
    if n < 3 or m < 3:
        return 0
    else:
        return 2 * (n // 3) * (m // 3) + (n % 3) * (m // 3) + (m % 3) * (n // 3)

# Read input
n, m = map(int, input().split())

# Calculate and print the result
print(max_chessmen(n, m))
