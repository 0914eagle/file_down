
def sort_even(l: list):
    even_indices = [val for idx, val in enumerate(l) if idx % 2 == 0]
    sorted_even_indices = sorted(even_indices)
    
    result = []
    for idx, val in enumerate(l):
        if idx % 2 == 0:
            result.append(sorted_even_indices.pop(0))
        else:
            result.append(val)
    
    return result

print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
