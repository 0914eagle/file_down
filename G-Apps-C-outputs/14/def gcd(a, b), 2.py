
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_probability(f, w, h):
    mod = 10**9 + 7
    total_arrangements = pow(2, f + w, mod) - 2
    good_arrangements = 0
    if h == 0:
        good_arrangements = total_arrangements
    elif h > 0:
        good_arrangements = pow(2, f, mod) * (pow(2, w, mod) - pow(2, w - h, mod))
    gcd_val = gcd(good_arrangements, total_arrangements)
    p = (good_arrangements // gcd_val) % mod
    q = (total_arrangements // gcd_val) % mod
    q_inv = pow(q, mod - 2, mod)
    result = (p * q_inv) % mod
    return result

# Input
f, w, h = map(int, input().split())

# Output
print(find_probability(f, w, h))
