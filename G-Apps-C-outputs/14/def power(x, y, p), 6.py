
def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y % 2 == 1:
            res = (res * x) % p
        y = y // 2
        x = (x * x) % p
    return res

def solve(f, w, h):
    MOD = 10**9 + 7
    total_arrangements = (f + w) * (f + w - 1)
    
    if h == 1:
        if w == 1:
            return 0
        else:
            favorable_arrangements = f + w
    else:
        favorable_arrangements = f + w
    
    gcd = power(total_arrangements, MOD - 2, MOD) # Calculate the modular inverse
    
    return (favorable_arrangements * gcd) % MOD

# Input
f, w, h = map(int, input().split())

# Output
print(solve(f, w, h))
