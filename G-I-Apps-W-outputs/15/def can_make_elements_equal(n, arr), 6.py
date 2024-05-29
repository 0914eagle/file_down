
def can_make_elements_equal(n, arr):
    arr.sort()
    if n == 1 or arr[0] == arr[-1]:
        return "YES"
    total_sum = sum(arr)
    min_val = arr[0]
    max_val = arr[-1]
    avg = total_sum / n
    if (total_sum % n == 0) and (min_val <= avg <= max_val):
        return "YES"
    return "NO"

# Read input
n = int(input())
arr = list(map(int, input().split()))

# Call the function and print the result
print(can_make_elements_equal(n, arr))
```
