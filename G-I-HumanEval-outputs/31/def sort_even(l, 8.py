
def sort_even(l: list):
    even_values = sorted([x for x in l if l.index(x) % 2 == 0])
    result = l.copy()
    for i in range(len(l)):
        if i % 2 == 0:
            result[i] = even_values.pop(0)
    return result

# Test cases
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]

