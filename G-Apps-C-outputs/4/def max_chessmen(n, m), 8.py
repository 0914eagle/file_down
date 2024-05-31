
def max_chessmen(n, m):
    if n < 2 or m < 2:
        return 0
    elif n == 2 or m == 2:
        return (n*m)//2 * 2
    else:
        return n*m - 2

# Read input
n, m = map(int, input().split())

# Calculate and print the result
print(max_chessmen(n, m))
