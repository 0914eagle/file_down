
def count_good_pairs(n, a, b):
    good_pairs = 0
    count_a = {}
    count_b = {}
    
    for i in range(n):
        if a[i] in count_a:
            count_a[a[i]] += 1
        else:
            count_a[a[i]] = 1
            
        if b[i] in count_b:
            count_b[b[i]] += 1
        else:
            count_b[b[i]] = 1
    
    for i in range(n):
        good_pairs += count_b[a[i]] - 1
        good_pairs += n - count_a[a[i]]
    
    return good_pairs // 2

# Input parsing
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Calculate and output the number of good pairs
print(count_good_pairs(n, a, b))
```
