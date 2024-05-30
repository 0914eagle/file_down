
def count_good_pairs(n, a, b):
    pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] + a[j] > b[i] + b[j]:
                pairs += 1
    return pairs

# Read input
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Call the function and print the result
print(count_good_pairs(n, a, b))
```
