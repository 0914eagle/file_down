
def count_good_pairs(n, a, b):
    good_pairs = 0
    a_diff = []
    b_diff = []
    
    for i in range(n):
        a_diff.append(a[i] - b[i])
        b_diff.append(b[i] - a[i])
    
    a_diff.sort()
    b_diff.sort()
    
    start = 0
    end = n - 1
    
    while start < n and end >= 0:
        if a_diff[start] > 0 and b_diff[end] > 0:
            good_pairs += end + 1
            start += 1
        else:
            end -= 1
            
    return good_pairs

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(count_good_pairs(n, a, b))
```
