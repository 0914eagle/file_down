
def binomial_coefficient_question(X):
    def binomial_coeff(n, k):
        if k == 0 or k == n:
            return 1
        else:
            return binomial_coeff(n-1, k-1) + binomial_coeff(n-1, k)

    n = 0
    while True:
        k = 0
        while k <= n:
            if binomial_coeff(n, k) == X:
                return n, k
            k += 1
        n += 1

# Input
X = int(input().strip())

# Output
n, k = binomial_coefficient_question(X)
print(n, k)
```
