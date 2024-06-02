
def is_sorted(lst):
    if len(lst) == 1:
        return True
    
    prev_num = lst[0]
    duplicate_count = 0
    
    for num in lst[1:]:
        if num < prev_num:
            return False
        elif num == prev_num:
            duplicate_count += 1
            if duplicate_count > 1:
                return False
        else:
            prev_num = num
            duplicate_count = 0
    
    return True

# Test cases
print(is_sorted([5]))  # ➞ True
print(is_sorted([1, 2, 3, 4, 5]))  # ➞ True
print(is_sorted([1, 3, 2, 4, 5]))  # ➞ False
print(is_sorted([1, 2, 3, 4, 5, 6]))  # ➞ True
print(is_sorted([1, 2, 3, 4, 5, 6, 7]))  # ➞ True
print(is_sorted([1, 3, 2, 4, 5, 6, 7]))  # ➞ False
print(is_sorted([1, 2, 2, 3, 3, 4]))  # ➞ True
print(is_sorted([1, 2, 2, 2, 3, 4]))  # ➞ False
