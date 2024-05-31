
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve(f, w, h):
    MOD = 10**9 + 7
    total_arrangements = f + w

    if h == 0:
        return pow(2, total_arrangements, MOD)

    if h > 1:
        return 0

    p = 0
    q = pow(2, total_arrangements, MOD)

    for i in range(1, w + 1):
        p = (p + pow(2, f, MOD) * pow(2, i - 1, MOD)) % MOD

    divisor = gcd(p, q)
    p //= divisor
    q //= divisor

    q_inverse = pow(q, MOD - 2, MOD)
    result = (p * q_inverse) % MOD

    return result

# Input
f, w, h = map(int, input().split())

# Output
print(solve(f, w, h))
