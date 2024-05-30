
def exponial(n, m):
    if n == 1:
        return 1
    
    def power_mod(a, b, mod):
        res = 1
        a %= mod
        while b > 0:
            if b % 2 == 1:
                res = (res * a) % mod
            b //= 2
            a = (a * a) % mod
        return res
    
    result = n
    for i in range(n - 1, 0, -1):
        result = power_mod(i, result, m)
    
    return result

n, m = map(int, input().split())
print(exponial(n, m))
```
