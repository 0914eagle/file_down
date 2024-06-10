
from functools import reduce
from math import gcd

MOD = 998244353

def inverse(x):
    return pow(x, MOD - 2, MOD)

def lcm(a, b):
    return a * b // gcd(a, b)

def solve(n, m, d, a, b):
    result = [0] * m
    for i in range(n):
        for j in range(m):
            if a[j] == 0:
                result[j] += d[i]
            elif a[j] > 0 and d[i] >= b[j]:
                a[j] -= 1
            elif a[j] > 0 and d[i] < b[j]:
                pass
    for i in range(m):
        result[i] %= MOD
    return result

def main():
    n, m = map(int, input().split())
    d = list(map(int, input().split()))
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    result = solve(n, m, d, a, b)
    for x in result:
        print(x)

if __name__ == '__main__':
    main()

