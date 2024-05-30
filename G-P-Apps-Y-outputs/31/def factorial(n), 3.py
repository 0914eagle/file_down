
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def combinations(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def number_of_ways(n):
    return combinations(n, n // 2) // (n // 2)

n = int(input())
print(number_of_ways(n))
```
