
def binomial_coefficients(X):
    n = 0
    k = 0
    while (n * (n + 1)) // 2 < X:
        n += 1

    while (n * k) < X:
        k += 1

    if n > 0 and k > 0 and n >= k and n * k == X:
        return n, k
    else:
        return -1, -1

# Example usage
X = 10
n, k = binomial_coefficients(X)
print(n, k)
```
