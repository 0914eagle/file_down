
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def probability_of_liking_arrangement(f, w, h):
    mod = 10**9 + 7
    total_arrangements = 2**f * 2**w - 2
    favorable_arrangements = (2**f - 1) * 2**w

    total_inverse = pow(total_arrangements, mod - 2, mod)
    favorable_inverse = pow(favorable_arrangements, mod - 2, mod)

    probability = (favorable_arrangements * favorable_inverse) % mod

    return probability

# Reading input
f, w, h = map(int, input().split())

# Calculating and printing the probability
print(probability_of_liking_arrangement(f, w, h))
