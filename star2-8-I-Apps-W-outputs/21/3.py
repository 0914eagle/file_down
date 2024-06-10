
n = int(input())
p = list(map(int, input().split()))

def solve(n, p):
    def inverse(a, m):
        a = a % m
        for x in range(m):
            if a * x % m == 1:
                return x
        return 1
    
    def C(n, k):
        if k < 0 or k > n:
            return 0
        res = 1
        for i in range(n - k + 1, n + 1):
            res *= i
        for i in range(1, k + 1):
            res //= i
        return res
    
    def P(n, k):
        if k < 0 or k > n:
            return 0
        res = 1
        for i in range(n - k + 1, n + 1):
            res *= i
        return res
    
    m = 998244353
    
    def fact(n):
        res = 1
        for i in range(1, n + 1):
            res *= i
            res %= m
        return res
    
    sum = 0
    
    for i in range(n):
        sum += C(n, i) * P(n, i) * (100 ** i) * (m - 100) ** (n - i) * inverse(100 ** n, m)
        sum %= m
    
    return sum

print(solve(n, p))

