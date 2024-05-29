
def can_make_equal_array(n, arr):
    total_sum = sum(arr)
    if total_sum % n == 0:
        return "YES"
    else:
        return "NO"

# Input processing
n = int(input())
arr = list(map(int, input().split()))

# Call the function and print the result
print(can_make_equal_array(n, arr))
```
