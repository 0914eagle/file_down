
def pluck(arr):
    even_values = [num for num in arr if num % 2 == 0]
    if not even_values:
        return []

    smallest_even = min(even_values)
    smallest_even_indices = [index for index, num in enumerate(arr) if num == smallest_even]

    return [smallest_even, min(smallest_even_indices)]

# Test cases
print(pluck([4, 2, 3]))  # Output: [2, 1]
print(pluck([1, 2, 3]))  # Output: [2, 1]
print(pluck([]))  # Output: []
print(pluck([5, 0, 3, 0, 4, 2]))  # Output: [0, 1]
```
