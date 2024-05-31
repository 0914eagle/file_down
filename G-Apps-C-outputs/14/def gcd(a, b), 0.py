
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def probability(f, w, h):
    MOD = 10**9 + 7
    p = q = 0
    
    for i in range(1, f + 1):
        if i > h:
            p += 1
        else:
            q += 1
    
    for i in range(1, w + 1):
        if i > h:
            p += 1
        else:
            q += 1
    
    total = pow(2, f + w, MOD) - 1
    inv_q = pow(q, MOD - 2, MOD)
    
    result = (p * inv_q) % MOD
    return result

# Input
f, w, h = map(int, input().split())

# Output
print(probability(f, w, h))
