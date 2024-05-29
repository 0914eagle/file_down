
def sort_even(l: list):
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    sorted_values = sorted([l[i] for i in even_indices])
    
    result = l.copy()
    for i, v in zip(even_indices, sorted_values):
        result[i] = v
    
    return result

# Test cases
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
