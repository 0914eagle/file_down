
n = int(input())

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def C(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

print(C(n, n//2)**2 // 2)

