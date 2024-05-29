
def sort_third(l: list):
    divisible_by_three = [v for i, v in enumerate(l) if i%3 == 0]
    sorted_divisible_by_three = sorted(divisible_by_three)
    
    result = l.copy()
    result[::3] = sorted_divisible_by_three

    return result

# Test cases
print(sort_third([1, 2, 3]))  # [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # [2, 6, 3, 4, 8, 9, 5]
