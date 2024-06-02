
def sort_third(l: list):
    divisible_by_three = [val for idx, val in enumerate(l) if idx % 3 == 0]
    sorted_divisible_by_three = sorted(divisible_by_three)
    result = [val if idx % 3 != 0 else sorted_divisible_by_three.pop(0) for idx, val in enumerate(l)]
    return result

# Test cases
print(sort_third([1, 2, 3]))  # [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # [2, 6, 3, 4, 8, 9, 5]
