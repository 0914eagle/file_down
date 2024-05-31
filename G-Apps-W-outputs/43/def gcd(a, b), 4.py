
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def count_good_pairs(l, r, x, y):
    count = 0
    for a in range(l, r + 1):
        if y % a == 0 and gcd(a, y // a) == x:
            count += 1
    return count

l, r, x, y = map(int, input().split())
print(count_good_pairs(l, r, x, y))
