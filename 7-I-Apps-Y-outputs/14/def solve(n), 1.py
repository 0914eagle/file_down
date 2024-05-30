
import math

def solve(n):
    k = math.log(n,2)
    k = math.ceil(k)
    x = n - (2**(k-1)) * (k-1)
    return x

t = int(input())
for i in range(t):
    n = int(input())
    x = solve(n)
    print(x)

