
def pluck(arr):
    even_values = [num for num in arr if num % 2 == 0]
    
    if not even_values:
        return []
    
    min_even = min(even_values)
    min_even_indices = [i for i, num in enumerate(arr) if num == min_even]
    
    return [min_even, min(min_even_indices)]

# Test cases
print(pluck([4, 2, 3]))  # Output: [2, 1]
print(pluck([1, 2, 3]))  # Output: [2, 1]
print(pluck([]))  # Output: []
print(pluck([5, 0, 3, 0, 4, 2]))  # Output: [0, 1]
```
