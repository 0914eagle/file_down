
def exponial_mod(n, m):
    def power_mod(base, exp, mod):
        if exp == 0:
            return 1
        if exp % 2 == 0:
            half_power = power_mod(base, exp // 2, mod)
            return (half_power * half_power) % mod
        else:
            return (base * power_mod(base, exp - 1, mod)) % mod
    
    result = 1
    for i in range(n, 0, -1):
        result = power_mod(i, result, m)
    
    return result

n, m = map(int, input().split())
print(exponial_mod(n, m))
```
