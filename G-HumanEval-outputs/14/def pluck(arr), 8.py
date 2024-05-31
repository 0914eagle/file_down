
def pluck(arr):
    if not arr:
        return []

    smallest_even = float('inf')
    smallest_index = len(arr)
    for i, num in enumerate(arr):
        if num % 2 == 0 and num < smallest_even:
            smallest_even = num
            smallest_index = i

    if smallest_index < len(arr):
        return [smallest_even, smallest_index]
    else:
        return []

# Test cases
print(pluck([4, 2, 3]))  # Output: [2, 1]
print(pluck([1, 2, 3]))  # Output: [2, 1]
print(pluck([]))  # Output: []
print(pluck([5, 0, 3, 0, 4, 2]))  # Output: [0, 1]
```
