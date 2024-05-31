
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def min_resistors(a, b):
    if a % b == 0:
        return a // b
    
    res = 0
    while b > 0:
        res += a // b
        a, b = b, a % b
    
    return res

# Input
a, b = map(int, input().split())

# Calculate the smallest possible number of resistors needed
print(min_resistors(a, b))
