
def sort_even(l: list):
    even_values = sorted([v for i, v in enumerate(l) if i % 2 == 0])
    l_modified = l.copy()
    for i in range(len(l)):
        if i % 2 == 0:
            l_modified[i] = even_values.pop(0)
    return l_modified

# Test cases
print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
