
def sort_even(l: list):
    odd_values = l[::2]
    even_values = sorted(l[1::2])
    result = [0] * (len(odd_values) + len(even_values))
    result[::2] = odd_values
    result[1::2] = even_values
    return result

# Test cases
print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
