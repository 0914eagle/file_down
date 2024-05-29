
def count_special_numbers(n, k):
    MOD = 10**9 + 7

    def count_set_bits(num):
        count = 0
        while num:
            count += 1
            num &= num - 1
        return count
    
    def count_special_numbers_util(num, operations_left):
        if num == 1 and operations_left == 0:
            return 1
        if num == 1 or operations_left == 0:
            return 0
        if dp[num][operations_left] != -1:
            return dp[num][operations_left]
        
        count = 0
        for i in range(1, num):
            count += count_special_numbers_util(num // i, operations_left - 1) % MOD
        
        dp[num][operations_left] = count % MOD
        return count
    
    n = int(n, 2)
    dp = [[-1] * (k + 1) for _ in range(n + 1)]
    return count_special_numbers_util(n, k)

n = input()
k = int(input())
print(count_special_numbers(n, k))
```
