
n = int(input())
p = list(map(int, input().split()))

def nCr(n, r): 
    return fact(n) / (fact(r) * fact(n - r))

def fact(n): 
    res = 1
    for i in range(2, n+1): 
        res = res * i 
    return res 

def nPr(n, r): 
    return fact(n) / fact(n - r)

prob = 0
for i in range(1, n+1):
    prob += p[i-1] * nCr(n, i) * (nPr(n-1, i-1) * (i-1) + nPr(n-1, i)) / 100

print(int(prob))

