
def pluck(arr):
    even_values = [num for num in arr if num % 2 == 0]
    
    if not even_values:
        return []
    
    smallest_value = min(even_values)
    smallest_index = arr.index(smallest_value)
    
    return [smallest_value, smallest_index]

# Test cases
print(pluck([4, 2, 3]))  # Output: [2, 1]
print(pluck([1, 2, 3]))  # Output: [2, 1]
print(pluck([]))  # Output: []
print(pluck([5, 0, 3, 0, 4, 2]))  # Output: [0, 1]
