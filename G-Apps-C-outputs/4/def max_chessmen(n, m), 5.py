
def max_chessmen(n, m):
    if n < 2 or m < 2:
        return 0
    if n == 2:
        return (m // 6) * 4 + min(2, m // 6) * 2
    if m == 2:
        return (n // 6) * 4 + min(2, n // 6) * 2
    return ((n * m) // 2) + ((n * m) % 2)

# Read input
n, m = map(int, input().split())

# Call the function and print the result
print(max_chessmen(n, m))
