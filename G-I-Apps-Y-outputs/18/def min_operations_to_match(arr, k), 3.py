
def min_operations_to_match(arr, k):
    min_val = min(arr)
    ops = 0
    while True:
        count = sum((num - min_val) // 2 for num in arr)
        if count >= k:
            return ops
        min_val //= 2
        ops += 1

n, k = map(int, input().split())
a = list(map(int, input().split()))

result = min_operations_to_match(a, k)
print(result)
```
