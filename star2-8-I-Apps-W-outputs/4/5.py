
n, m = map(int, input().split())
MOD = 10 ** 9 + 7

def solve(n: int, m: int) -> int:
    def factorize(m: int) -> dict:
        factors = dict()
        i = 2
        while i * i <= m:
            while m % i == 0:
                m //= i
                factors[i] = factors.get(i, 0) + 1
            i += 1
        if m != 1:
            factors[m] = factors.get(m, 0) + 1
        return factors
    
    factors = factorize(m)
    res = 1
    for f in factors:
        res *= factors[f] + 1
        res %= MOD
    
    return res

print(solve(n, m))

