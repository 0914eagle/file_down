
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def count_good_pairs(l, r, x, y):
    gcd_lcm = gcd(x, y)
    lcm_gcd = lcm(x, y)
    count = 0

    for a in range(max(x, l // gcd_lcm), min(y, r // lcm_gcd) + 1):
        b_lower = max(l, a * gcd_lcm)
        b_upper = min(r, a * lcm_gcd)
        count += max(0, (b_upper - b_lower) // gcd_lcm + 1)

    return count

l, r, x, y = map(int, input().split())
print(count_good_pairs(l, r, x, y))
