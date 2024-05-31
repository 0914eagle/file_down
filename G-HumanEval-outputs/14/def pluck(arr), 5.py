
def pluck(arr):
    smallest_even = None
    smallest_even_index = None
    
    for i, num in enumerate(arr):
        if num % 2 == 0 and (smallest_even is None or num < smallest_even or (num == smallest_even and i < smallest_even_index)):
            smallest_even = num
            smallest_even_index = i

    if smallest_even is not None:
        return [smallest_even, smallest_even_index]
    else:
        return []

# Test cases
print(pluck([4, 2, 3]))  # Output: [2, 1]
print(pluck([1, 2, 3]))  # Output: [2, 1]
print(pluck([]))  # Output: []
print(pluck([5, 0, 3, 0, 4, 2]))  # Output: [0, 1]
```
