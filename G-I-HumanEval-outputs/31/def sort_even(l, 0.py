
def sort_even(l: list):
    # Get the even indexed values from the original list
    even_values = sorted(l[::2])
    
    # Create a new list with odd indexed values same as the original list
    result = l[:]
    
    # Replace the even indexed values in the new list with the sorted values
    result[::2] = even_values
    
    return result

# Test cases
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
