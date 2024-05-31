
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def min_resistors(a, b):
    if a == b:
        return 1

    if a < b:
        a, b = b, a

    res = a // b
    a %= b

    if a == 0:
        return res

    return res + min_resistors(b, a)

# Input
a, b = map(int, input().split())

# Calculate the answer and output
print(min_resistors(a, b))
