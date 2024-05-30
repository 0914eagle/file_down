
def expected_unique_elements(n, arr):
    total_sum = sum(set(arr))
    expected = total_sum * (n+1) / (2*n)
    return expected

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
print("{:.6f}".format(expected_unique_elements(n, arr)))
```
