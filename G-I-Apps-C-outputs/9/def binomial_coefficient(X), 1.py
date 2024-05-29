
def binomial_coefficient(X):
    n = 0
    while True:
        n += 1
        k = 0
        while k <= n:
            if factorial(n) // (factorial(k) * factorial(n - k)) == X:
                return n, k
            k += 1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

X = int(input())
n, k = binomial_coefficient(X)
print(n, k)
```
