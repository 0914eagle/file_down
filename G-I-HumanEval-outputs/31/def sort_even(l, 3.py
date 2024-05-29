
def sort_even(l: list):
    even_values = sorted([x for i, x in enumerate(l) if i % 2 == 0])
    result = [x for i, x in enumerate(l) if i % 2 != 0]
    for i, x in enumerate(l):
        if i % 2 == 0:
            result.append(even_values.pop(0))
    return result

# Test cases
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
