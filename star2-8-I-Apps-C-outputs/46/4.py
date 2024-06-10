
import sys

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
def chinese_remainder(n, a):
    prod = 1
    for i in range(len(n)):
        prod *= n[i]
    result = 0
    for i in range(len(n)):
        p = prod // n[i]
        result += a[i] * mul_inv(p, n[i]) * p
    return result % prod
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1

m,x,y=map(int,input().split()),map(int,input().split()),map(int,input().split())
a=chinese_remainder(m,x)
n=[i*i for i in m]
print(min(a+i for i in range(-3,4) for a in (a+i*j for j in n) if all(a%m[i]==x[i]+i*y[i] for i in range(3))))

