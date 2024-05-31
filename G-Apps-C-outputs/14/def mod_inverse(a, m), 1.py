
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def calculate_probability(f, w, h):
    total_arrangements = pow(2, f + w, 10**9 + 7) - 2
    invalid_arrangements = 0

    for i in range(1, h + 1):
        invalid_arrangements += (pow(2, f, 10**9 + 7) * pow(2, w, 10**9 + 7 - pow(2, i, 10**9 + 7))) % (10**9 + 7)

    valid_arrangements = total_arrangements - invalid_arrangements
    mod_inv = mod_inverse(total_arrangements, 10**9 + 7)
    probability = (valid_arrangements * mod_inv) % (10**9 + 7)

    return probability

# Input
f, w, h = map(int, input().split())

# Output
print(calculate_probability(f, w, h))
