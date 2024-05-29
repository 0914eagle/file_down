
def count_special_numbers(n, k):
    mod = 10**9 + 7
    
    def count_set_bits(num):
        count = 0
        while num:
            num &= num - 1
            count += 1
        return count
    
    def dp(i, b, is_less, is_zero, is_equal):
        if i == len(n):
            return 1 if not is_zero else 0
        
        if not is_less and not is_zero and not is_equal:
            if i == len(n) - 1:
                return count_set_bits(b) == k
            
            if dp(i+1, b | (1 << (len(n) - i - 2)), False, False, n[i+1:] == '0'*(len(n)-i-1):
                return 1
        
        res = 0
        max_d = 1 if is_less else int(n[i])
        for d in range(max_d + 1):
            res = (res + dp(i+1, b | (d << (len(n) - i - 1)), is_less or d < max_d, is_zero and d == 0, is_equal and d == int(n[i]))) % mod
        
        return res
    
    return dp(0, 0, False, True, True)

# Input reading and processing
n = input().strip()
k = int(input().strip())
print(count_special_numbers(n, k))
```
