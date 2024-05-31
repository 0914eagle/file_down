
def next_smallest(lst):
    if len(lst) < 2:
        return None
    else:
        unique_nums = list(set(lst))
        unique_nums.sort()
        if len(unique_nums) < 2:
            return None
        else:
            return unique_nums[1]
        
# Test cases
print(next_smallest([1, 2, 3, 4, 5]))  # 2
print(next_smallest([5, 1, 4, 3, 2]))  # 2
print(next_smallest([]))  # None
print(next_smallest([1, 1]))  # None
