
def find_max_chessmen(n, m):
    if n < 3 or m < 3:
        return 0
    elif n == 1 or m == 1:
        return (n * m) // 2 * 2
    else:
        return (n * m) // 2 * 2 + min(n % 2, m % 2) * 2

# Read input
n, m = map(int, input().split())

# Calculate and print the result
print(find_max_chessmen(n, m))
