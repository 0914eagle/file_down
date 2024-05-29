
def max_element(l: list):
    
    if not l:
        return None
    max_val = l[0]
    for i in range(1, len(l)):
        if l[i] > max_val:
            max_val = l[i]
    return max_val

# Test cases
print(max_element([1, 2, 3]))  # 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # 123
