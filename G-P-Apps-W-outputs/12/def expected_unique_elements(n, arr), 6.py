
def expected_unique_elements(n, arr):
    total_unique = len(set(arr))
    expected = 0
    for i in range(n):
        for j in range(i, n):
            l = min(i+1, j+1)
            r = max(i+1, j+1)
            segment_unique = len(set(arr[l-1:r]))
            prob = 1 / (n * (n + 1) / 2)
            expected += prob * segment_unique
    return expected

n = int(input())
arr = list(map(int, input().split()))
result = expected_unique_elements(n, arr)
print("{:.6f}".format(result))
```
