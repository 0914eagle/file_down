
def power(a, b, MOD):
    result = 1
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % MOD
        a = (a * a) % MOD
        b //= 2
    return result

def solve(f, w, h):
    MOD = 10**9 + 7
    total_arrangements = power(2, f + w, MOD)
    
    if h == 0:
        return total_arrangements
    
    favorable_arrangements = 0
    
    if f >= h:
        favorable_arrangements += power(2, f - h, MOD)
    
    if w >= h:
        favorable_arrangements += power(2, w - h, MOD)
    
    return (favorable_arrangements * power(total_arrangements, MOD - 2, MOD)) % MOD

f, w, h = map(int, input().split())
print(solve(f, w, h))
