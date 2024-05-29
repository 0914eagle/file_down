
def smallest_change(arr):
    def is_palindrome(arr):
        return arr == arr[::-1]

    changes = 0
    left, right = 0, len(arr) - 1

    while left < right:
        if arr[left] != arr[right]:
            changes += 1
        left += 1
        right -= 1

    return changes

# Test cases
print(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]))  # Output should be 4
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))  # Output should be 1
print(smallest_change([1, 2, 3, 2, 1]))  # Output should be 0
