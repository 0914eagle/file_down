
def count_good_pairs(n, a, b):
    total_pairs = 0
    good_pairs = 0
    
    for i in range(n):
        for j in range(i+1, n):
            total_pairs += 1
            if a[i] + a[j] > b[i] + b[j]:
                good_pairs += 1
    
    return good_pairs

# Read input
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Call the function and print the result
print(count_good_pairs(n, a, b))
```
