
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def min_resistors(a, b):
    if b % a == 0:
        return b // a
    
    g = gcd(a, b)
    a //= g
    b //= g
    return b + min_resistors(b, a)

# Input
a, b = map(int, input().split())

# Output
print(min_resistors(a, b))
