
def count_monotonic_renumerations(n, a):
    mod = 998244353
    freq = {}
    for num in a:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    counts = list(freq.values())
    counts.sort()
    
    if counts[0] == n:
        return 1
    
    ans = 1
    for count in counts:
        ans = (ans * count) % mod
    
    return ans

# Input
n = int(input())
a = list(map(int, input().split()))

# Output
print(count_monotonic_renumerations(n, a))
```
