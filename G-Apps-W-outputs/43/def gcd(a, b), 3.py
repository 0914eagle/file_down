
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def count_good_pairs(l, r, x, y):
    num_good_pairs = 0
    for a in range(l, r + 1):
        if y % a == 0 and gcd(a, y // a) == x:
            num_good_pairs += 1
    return num_good_pairs

# Input parsing
l, r, x, y = map(int, input().split())

# Call the function and print the result
print(count_good_pairs(l, r, x, y))
