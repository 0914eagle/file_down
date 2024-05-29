
def can_make_all_elements_equal(n, arr):
    min_val = min(arr)
    max_val = max(arr)
    if (max_val - min_val) % 2 == 0:
        x = (max_val + min_val) // 2
        for num in arr:
            if num != min_val and num != max_val and num != x:
                return "NO"
        return "YES"
    else:
        for num in arr:
            if num != min_val and num != max_val:
                return "NO"
        return "YES"

# Input reading
n = int(input())
arr = list(map(int, input().split()))

# Check if it's possible and print the output
print(can_make_all_elements_equal(n, arr))
```
