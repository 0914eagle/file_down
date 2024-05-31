
def smallest_change(arr):
    def is_palindromic(array):
        return array == array[::-1]

    count = 0
    for i in range(len(arr)//2):
        if arr[i] != arr[-1-i]:
            count += 1

    return count

# Test cases
print(smallest_change([1,2,3,5,4,7,9,6]))  # Output: 4
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))  # Output: 1
print(smallest_change([1, 2, 3, 2, 1]))  # Output: 0
```
