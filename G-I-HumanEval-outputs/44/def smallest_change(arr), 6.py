
def smallest_change(arr):
    def is_palindrome(sub_arr):
        return sub_arr == sub_arr[::-1]

    length = len(arr)

    if is_palindrome(arr):
        return 0

    changes = 0
    for i in range(length // 2):
        if arr[i] != arr[length - 1 - i]:
            changes += 1

    return changes

# Test cases
print(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]))  # Output: 4
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))  # Output: 1
print(smallest_change([1, 2, 3, 2, 1]))  # Output: 0
```
