
import sys
def get_min_ops(nums):
    sorted_nums = sorted(nums)
    min_ops = 0
    i, j = 0, len(nums) - 1
    while i < len(nums) and j >= 0:
        if nums[i] == sorted_nums[i]:
            i += 1
        elif nums[j] == sorted_nums[j]:
            j -= 1
        else:
            min_ops += 1
        if i > j:
            break
    return min_ops
nums = [int(x) for x in sys.stdin.readline().strip().split()]
min_ops = get_min_ops(nums)
print(min_ops)

