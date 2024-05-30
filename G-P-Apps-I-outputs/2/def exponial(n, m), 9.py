
def exponial(n, m):
    def power_mod(a, b, m):
        if b == 0:
            return 1
        if b % 2 == 0:
            return power_mod(a * a % m, b // 2, m)
        return a * power_mod(a, b - 1, m) % m
    
    def exponial_helper(n, m):
        if n == 1:
            return 1
        return power_mod(n, exponial_helper(n - 1, m), m)
    
    return exponial_helper(n, m)

n, m = map(int, input().split())
print(exponial(n, m))
```
