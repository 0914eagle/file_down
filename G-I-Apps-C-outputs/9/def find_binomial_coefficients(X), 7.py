
def find_binomial_coefficients(X):
    n = 0
    while True:
        n += 1
        for k in range(min(n, X)):
            if binomial_coefficient(n, k) == X:
                return n, k

def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)

X = int(input().strip())
n, k = find_binomial_coefficients(X)
print(n, k)
```
