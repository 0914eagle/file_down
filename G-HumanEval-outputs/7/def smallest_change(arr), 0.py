
def smallest_change(arr):
    def is_palindrome(lst):
        return lst == lst[::-1]
    
    changes = 0
    left = 0
    right = len(arr) - 1
    
    while left < right:
        if arr[left] != arr[right]:
            if arr[left] < arr[right]:
                arr[left] = arr[right]
            else:
                arr[right] = arr[left]
            changes += 1
        left += 1
        right -= 1
    
    return changes

# Test cases
print(smallest_change([1,2,3,5,4,7,9,6]))  # Output: 4
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))  # Output: 1
print(smallest_change([1, 2, 3, 2, 1]))  # Output: 0
