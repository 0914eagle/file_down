
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solve(a, b):
    if a == b:
        return 1
    if a < b:
        return solve(a, b - a) + 1
    g = gcd(a, b)
    return a // g

# Input
a, b = map(int, input().split())

# Output
print(solve(a, b))
