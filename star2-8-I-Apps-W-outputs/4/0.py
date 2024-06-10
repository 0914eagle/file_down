
def factorize(n):
    res = []
    while n > 1:
        for p in range(2, n + 1):
            if n % p == 0:
                res.append(p)
                n //= p
                break
    return res

def solve():
    N, M = map(int, input().split())
    primes = factorize(M)
    res = 1
    for p in primes:
        cnt = 0
        while p**cnt <= M:
            cnt += 1
        res *= cnt
        res %= 10**9 + 7
    print(res)

solve()

