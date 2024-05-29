
def sort_even(l: list):
    even_vals = sorted([val for idx, val in enumerate(l) if idx % 2 == 0])
    result = []
    for idx, val in enumerate(l):
        if idx % 2 == 0:
            result.append(even_vals.pop(0))
        else:
            result.append(val)
    return result

# Test cases
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
