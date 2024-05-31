
def max_chessmen(n, m):
    if n < 3 or m < 3:
        return 0

    even_rows = n // 2
    odd_rows = n - even_rows

    even_cols = m // 2
    odd_cols = m - even_cols

    total_pairs = (even_rows * even_cols) + (odd_rows * odd_cols)

    return total_pairs * 2

# Read input
n, m = map(int, input().split())

# Calculate and print the result
print(max_chessmen(n, m))
