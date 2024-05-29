
from math import comb

def find_binomial_coefficients(X):
    n, k = 0, 0
    while comb(n, k) != X:
        if k < n:
            k += 1
        else:
            n += 1
            k = 0
    return n, k

X = int(input())
n, k = find_binomial_coefficients(X)
print(n, k)
```
