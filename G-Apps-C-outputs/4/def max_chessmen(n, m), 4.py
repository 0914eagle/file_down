
def max_chessmen(n, m):
    if n < 2 or m < 2:
        return 0
    elif n == 2 or m == 2:
        return (n * m) // 2 * 4
    else:
        return (n * m) // 2 * 4 + 2

# Input
n, m = map(int, input().split())

# Output
print(max_chessmen(n, m))
