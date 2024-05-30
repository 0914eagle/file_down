
def exponial(n, m):
    if n == 1:
        return 1
    
    def fast_pow(base, exp, mod):
        result = 1
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % mod
            base = (base * base) % mod
            exp //= 2
        return result

    ans = n
    for i in range(n-1, 0, -1):
        ans = fast_pow(i, ans, m)
    
    return ans % m

# Read input
n, m = map(int, input().split())

# Calculate and output the result
print(exponial(n, m))
```
