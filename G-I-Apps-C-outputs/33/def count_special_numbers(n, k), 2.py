
MOD = 10**9 + 7

def count_special_numbers(n, k):
    memo = {}

    def get_bits(num):
        return bin(num).count('1')
    
    def dp(num, steps):
        if num == 1:
            return 1 if steps == k else 0
        if steps > k:
            return 0
        if (num, steps) in memo:
            return memo[(num, steps)]
        
        total = 0
        for i in range(num, 0, -1):
            bits = get_bits(i)
            total = (total + dp(i, steps + bits)) % MOD
        
        memo[(num, steps)] = total
        return total

    return dp(n, 0)

# Input
n = int(input(), 2)
k = int(input())

# Output
print(count_special_numbers(n, k))
```
