
def count_good_pairs(n, a, b):
    count = 0
    good_pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] + a[j] > b[i] + b[j]:
                good_pairs += 1
    return good_pairs

# Input processing
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Output
print(count_good_pairs(n, a, b))
```
