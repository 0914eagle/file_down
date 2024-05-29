
def binomial_coefficient_problem(X):
    n = 1
    while True:
        k = 1
        while k <= n:
            if calculate_binomial_coefficient(n, k) == X:
                return n, k
            k += 1
        n += 1

def calculate_binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    return calculate_binomial_coefficient(n-1, k-1) + calculate_binomial_coefficient(n-1, k)

# Input
X = int(input())

# Output
n, k = binomial_coefficient_problem(X)
print(n, k)
```
