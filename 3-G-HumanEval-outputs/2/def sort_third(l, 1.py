
def sort_third(l: list):
    sorted_indices = [i for i in range(len(l)) if i % 3 == 0]
    sorted_values = [l[i] for i in sorted_indices]
    sorted_values.sort()
    
    result = l.copy()
    for i in sorted_indices:
        result[i] = sorted_values.pop(0)
    
    return result

# Test cases
print(sort_third([1, 2, 3]))  # [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # [2, 6, 3, 4, 8, 9, 5]
