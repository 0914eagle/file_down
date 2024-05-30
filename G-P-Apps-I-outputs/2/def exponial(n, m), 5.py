
def exponial(n, m):
    def power_mod(a, b, m):
        if b == 0:
            return 1
        if b % 2 == 0:
            return power_mod((a * a) % m, b // 2, m)
        else:
            return (a * power_mod(a, b - 1, m)) % m

    result = 1
    for i in range(n-1, 0, -1):
        result = power_mod(i, result, m)

    return result % m

# Input
n, m = map(int, input().split())

# Output
print(exponial(n, m))
```
