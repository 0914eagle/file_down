
def smallest_change(arr):
    def is_palindrome(lst):
        return lst == lst[::-1]

    changes = 0
    for i in range(len(arr) // 2):
        if arr[i] != arr[-i - 1]:
            changes += 1

    return changes

# Test cases
print(smallest_change([1,2,3,5,4,7,9,6]))  # Output: 4
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))  # Output: 1
print(smallest_change([1, 2, 3, 2, 1]))  # Output: 0
