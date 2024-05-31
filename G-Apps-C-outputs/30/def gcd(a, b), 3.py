
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def min_resistors(a, b):
    if a == b:
        return 1

    if a > b:
        return min_resistors(a - b, b) + 1
    else:
        gcd_val = gcd(a, b)
        return min_resistors(a, b - a) * (b // gcd_val) + min_resistors(a, b - a) * (a // gcd_val)

# Read input
a, b = map(int, input().split())

# Output the result
print(min_resistors(a, b))
