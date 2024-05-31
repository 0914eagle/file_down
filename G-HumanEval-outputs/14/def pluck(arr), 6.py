
def pluck(arr):
    even_values = [(i, v) for i, v in enumerate(arr) if v % 2 == 0]
    
    if not even_values:
        return []
    
    min_even = min(even_values, key=lambda x: x[1])
    min_even_indices = [x for x in even_values if x[1] == min_even[1]]
    
    return min(min_even_indices, key=lambda x: x[0])

# Test cases
print(pluck([4, 2, 3]))  # Output: [2, 1]
print(pluck([1, 2, 3]))  # Output: [2, 1]
print(pluck([]))          # Output: []
print(pluck([5, 0, 3, 0, 4, 2]))  # Output: [0, 1]
```
