
def min_integers_to_insert(n, arr):
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]
    
    freq = {}
    for s in prefix_sum:
        if s not in freq:
            freq[s] = 1
        else:
            freq[s] += 1
    
    max_freq = max(freq.values())
    
    return n - max_freq

# Input reading
n = int(input())
arr = list(map(int, input().split()))

# Function call and output
print(min_integers_to_insert(n, arr))
```
