
MOD = 998244353

def count_monotonic_renumerations(n, a):
    freq = {}
    for num in a:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    max_freq = max(freq.values())
    num_diff_nums = len(freq)
    
    if max_freq > (n + 1) // 2 or (max_freq == (n + 1) // 2 and num_diff_nums % 2 == 0):
        return 0
    
    total = 1
    for key in freq:
        total = (total * freq[key]) % MOD
    
    return total

# Reading input
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(count_monotonic_renumerations(n, a))
```
