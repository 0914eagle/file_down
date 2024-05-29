
def sort_third(l: list):
    result = l.copy()
    indices_divisible_by_three = [i for i in range(len(l)) if i % 3 == 0]
    values_to_sort = [l[i] for i in indices_divisible_by_three]
    sorted_values = sorted(values_to_sort)
    
    for i, j in zip(indices_divisible_by_three, range(len(sorted_values))):
        result[i] = sorted_values[j]
    
    return result

# Test cases
print(sort_third([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # Output: [2, 6, 3, 4, 8, 9, 5]
