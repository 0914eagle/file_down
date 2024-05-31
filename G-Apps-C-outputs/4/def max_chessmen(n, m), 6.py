
def max_chessmen(n, m):
    if n < 2 or m < 2:
        return 0
    return (n // 2) * (m // 2) * 2

# Input processing
n, m = map(int, input().split())

# Output
print(max_chessmen(n, m))
