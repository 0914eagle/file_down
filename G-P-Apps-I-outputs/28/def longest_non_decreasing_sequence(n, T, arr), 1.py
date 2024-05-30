
def longest_non_decreasing_sequence(n, T, arr):
    arr_len = len(arr)
    max_len = 1
    for i in range(arr_len):
        cur_len = 1
        j = i
        while j < arr_len - 1 and arr[j] <= arr[j + 1]:
            cur_len += 1
            j += 1
        max_len = max(max_len, cur_len)
    return max_len * T

# Input processing
n, T = map(int, input().split())
arr = list(map(int, input().split()))

# Call the function and print the result
print(longest_non_decreasing_sequence(n, T, arr))
```
