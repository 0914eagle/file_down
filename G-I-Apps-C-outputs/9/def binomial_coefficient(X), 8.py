
def binomial_coefficient(X):
    n = 0
    while True:
        n += 1
        k = 0
        while k <= n:
            if binomial(n, k) == X:
                return n, k
            k += 1

def binomial(n, k):
    if k == 0 or k == n:
        return 1
    return binomial(n - 1, k - 1) + binomial(n - 1, k)

# Input
X = int(input())

# Output
n, k = binomial_coefficient(X)
print(n, k)
```
