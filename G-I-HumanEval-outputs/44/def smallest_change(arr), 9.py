
def smallest_change(arr):
    def is_palindromic(possible_palindrome):
        return possible_palindrome == possible_palindrome[::-1]

    changes_needed = 0
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - 1 - i]:
            changes_needed += 1

    return changes_needed

# Test cases
print(smallest_change([1,2,3,5,4,7,9,6]))  # Output should be 4
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))  # Output should be 1
print(smallest_change([1, 2, 3, 2, 1]))  # Output should be 0
```
