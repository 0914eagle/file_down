
def next_smallest(lst):
    if len(lst) < 2:
        return None
    
    unique_nums = sorted(set(lst))
    
    if len(unique_nums) < 2:
        return None
    
    return unique_nums[1]
