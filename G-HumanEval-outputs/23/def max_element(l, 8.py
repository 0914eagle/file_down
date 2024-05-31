
def max_element(l: list):
    
    if not l:
        return None
    max_val = l[0]
    for num in l:
        if num > max_val:
            max_val = num
    return max_val

# Test cases
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```
