
def make_elements_equal(n, arr):
    total_sum = sum(arr)
    max_element = max(arr)
    min_element = min(arr)

    if (total_sum % n != 0) or (max_element - min_element > total_sum // n):
        return "NO"
    else:
        return "YES"

# Input processing
n = int(input())
arr = list(map(int, input().split()))

# Call the function and output the result
print(make_elements_equal(n, arr))
```
