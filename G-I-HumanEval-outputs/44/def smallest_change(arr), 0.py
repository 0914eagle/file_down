
def smallest_change(arr):
    # Helper function to check if an array is palindromic
    def is_palindromic(array):
        return array == array[::-1]

    # Initialize counters for minimum changes and left and right pointers
    changes = 0
    left = 0
    right = len(arr) - 1

    # Iterate through the array while left pointer is less than right pointer
    while left < right:
        # If elements at left and right pointers are not equal
        if arr[left] != arr[right]:
            # Increment changes by 1
            changes += 1
            # Decide which element to change to make them equal and move pointers accordingly
            if arr[left] < arr[right]:
                arr[left] = arr[right]
            else:
                arr[right] = arr[left]
        
        # Move pointers towards the center
        left += 1
        right -= 1

    return changes

# Test cases
print(smallest_change([1,2,3,5,4,7,9,6]))  # Output: 4
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))  # Output: 1
print(smallest_change([1, 2, 3, 2, 1]))  # Output: 0
