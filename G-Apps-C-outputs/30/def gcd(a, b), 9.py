
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def min_resistors(a, b):
    if a < b:
        a, b = b, a

    if a % b == 0:
        return a // b

    common_divisor = gcd(a, b)
    a //= common_divisor
    b //= common_divisor

    return b + min_resistors(a, b)

# Read input
a, b = map(int, input().split())
# Calculate and print output
print(min_resistors(a, b))
