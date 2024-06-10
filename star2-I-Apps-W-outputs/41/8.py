
from math import factorial

def catalan(n):
    return factorial(2 * n) // (factorial(n) * factorial(n + 1))

def square_catalan(n):
    return sum(catalan(k) * catalan(n - k) for k in range(n + 1))

n = int(input())
print(square_catalan(n))

