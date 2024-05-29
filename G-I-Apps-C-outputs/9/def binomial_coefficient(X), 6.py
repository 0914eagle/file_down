
def binomial_coefficient(X):
    n = 0
    while True:
        n += 1
        k = 0
        while k <= n:
            result = factorial(n) // (factorial(k) * factorial(n - k))
            if result == X:
                return n, k
            k += 1

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

X = int(input())
n, k = binomial_coefficient(X)
print(n, k)
```
