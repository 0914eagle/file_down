
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solve(f, w, h):
    MOD = 10**9 + 7
    q_inv = pow(2, MOD - 2, MOD)  # Calculate the modular inverse of 2

    total_arrangements = (f + 1) * (w + 1)  # Total number of arrangements
    favourable_arrangements = 0

    for i in range(0, f + 1):
        for j in range(0, w + 1):
            if i > 0 and j > 0:
                favourable_arrangements += 2  # Both food and wine stack can be at the current position
            else:
                favourable_arrangements += 1  # Either only food or only wine stack can be at the current position

    ans = favourable_arrangements * pow(total_arrangements, MOD - 2, MOD) % MOD

    return ans

# Input
f, w, h = map(int, input().split())

# Output
print(solve(f, w, h))
