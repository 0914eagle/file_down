
from math import factorial

def C(n):
    return factorial(2*n)//(factorial(n)*factorial(n+1))

def S(n):
    return sum(C(k)*C(n-k) for k in range(n+1))

print(S(int(input())))

