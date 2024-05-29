
def binomial_coefficients(X):
    n = 0
    while True:
        n += 1
        k = 0
        while k <= n:
            if binomial_coefficient(n, k) == X:
                return n, k
            k += 1

def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)

# Input
X = int(input())
n, k = binomial_coefficients(X)

# Output
print(n, k)
```
