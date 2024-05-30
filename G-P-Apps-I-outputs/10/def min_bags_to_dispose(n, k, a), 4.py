
def min_bags_to_dispose(n, k, a):
    bags = 0
    remaining = 0

    for i in range(n):
        total_garbage = a[i] + remaining
        bags += total_garbage // k
        remaining = total_garbage % k

    if remaining > 0:
        bags += 1

    return bags

# Input processing
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Call the function and output the result
print(min_bags_to_dispose(n, k, a))
```
