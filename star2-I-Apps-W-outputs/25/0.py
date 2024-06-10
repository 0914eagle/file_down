
import sys
from functools import reduce

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def main():
    n, m = map(int, input().split())
    d = list(map(int, input().split()))
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    
    mod = 998244353
    
    for i in range(m):
        damage = 0
        for j in range(n):
            if a[i] == 0:
                damage += d[j]
            elif a[i] > 0 and d[j] >= b[i]:
                a[i] -= 1
            elif a[i] > 0 and d[j] < b[i]:
                pass
        
        if damage == 0:
            print(0)
        else:
            g = reduce(lambda x, y: math.gcd(x, y), d)
            damage //= g
            modinv_damage = modinv(damage, mod)
            print((damage * modinv_damage) % mod)

if __name__ == '__main__':
    main()

