
n = int(input())

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

def C(n, k):
    return fact(n) // (fact(k) * fact(n - k))

print(C(n, n // 2) * C(n, n // 2))

