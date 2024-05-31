
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def probability_of_liking_arrangement(f, w, h):
    mod = 10**9 + 7

    total_arrangements = pow(2, f + w, mod) - 1

    favorable_arrangements = 0

    if h == 0:
        favorable_arrangements = total_arrangements
    elif h > 1:
        favorable_arrangements = total_arrangements
    else:
        favorable_arrangements = f * w

    gcd_val = gcd(favorable_arrangements, total_arrangements)
    p = favorable_arrangements // gcd_val
    q = total_arrangements // gcd_val

    inverse_q = pow(q, mod - 2, mod)

    return (p * inverse_q) % mod

# Input parsing
f, w, h = map(int, input().split())

# Call the function with the given input
result = probability_of_liking_arrangement(f, w, h)
print(result)
