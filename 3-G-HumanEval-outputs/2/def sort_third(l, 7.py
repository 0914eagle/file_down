
def sort_third(l: list):
    result = l.copy()
    indices_divisible_by_three = [i for i in range(len(l)) if i % 3 == 0]
    values_divisible_by_three = [l[i] for i in indices_divisible_by_three]
    sorted_values = sorted(values_divisible_by_three)
    
    for i, val in zip(indices_divisible_by_three, sorted_values):
        result[i] = val
    
    return result

# Test cases
print(sort_third([1, 2, 3]))  # [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # [2, 6, 3, 4, 8, 9, 5]
