
n = int(input())

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def combinations(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

def solve(n):
    return combinations(n, n//2) ** 2

print(solve(n))

