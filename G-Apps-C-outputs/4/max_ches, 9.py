max_chessmen(n, m):
    if n < 3 or m < 3:
        return 0
    else:
        return (n // 3) * (m // 3) * 2 + ((n % 3) * (m // 3)) + ((m % 3) * (n // 3))

# Read input
n, m = map(int, input().split())

# Output the result
print(max_chessmen(n, m))
