
def sort_even(l: list):
    even_indices = [l[i] for i in range(len(l)) if i % 2 == 0]
    sorted_even_values = sorted(even_indices)
    
    result = []
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(sorted_even_values.pop(0))
        else:
            result.append(l[i])
    return result

# Test cases
print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
