
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def min_resistors(a, b):
    if a == b:
        return 1

    if a < b:
        return 1 + min_resistors(a, b - a)
    else:
        return (a // b) + min_resistors(a % b, b)

a, b = map(int, input().split())
print(min_resistors(a, b))
