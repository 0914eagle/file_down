
def expected_unique_elements(n, arr):
    total_unique = len(set(arr))
    expected = 0
    for i in range(n):
        for j in range(i, n):
            expected += len(set(arr[i:j+1])) / (n*(n+1)/2)
    return expected

n = int(input())
arr = list(map(int, input().split()))
result = expected_unique_elements(n, arr)
print("{:.6f}".format(result))
```
