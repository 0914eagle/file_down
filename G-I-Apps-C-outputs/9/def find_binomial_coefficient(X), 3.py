
def find_binomial_coefficient(X):
    n = 0
    while True:
        n += 1
        k = 0
        while k <= n:
            if k == 0 or k == n:
                coeff = 1
            else:
                coeff = factorial(n) // (factorial(k) * factorial(n - k))
            if coeff == X:
                return n, k
            k += 1

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Input
X = int(input())

# Find and print the solution
n, k = find_binomial_coefficient(X)
print(n, k)
```
