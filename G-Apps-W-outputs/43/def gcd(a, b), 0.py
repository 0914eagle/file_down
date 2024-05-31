
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def count_good_pairs(l, r, x, y):
    count = 0
    for a in range(l, r+1):
        b = y // gcd(a, y)
        if l <= a <= r and l <= b <= r and gcd(a, b) == x and lcm(a, b) == y:
            count += 1
    return count

# Input
l, r, x, y = map(int, input().split())
# Output
print(count_good_pairs(l, r, x, y))
