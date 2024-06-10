
n = int(input())
nums = [int(x) for x in input().split()]

def find_swaps(nums):
    swaps = []
    for i in range(n):
        min_val = min(nums)
        min_idx = nums.index(min_val)
        if min_idx != i:
            swaps.append((i, min_idx))
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return swaps

swaps = find_swaps(nums)
print(len(swaps))
for swap in swaps:
    print(swap[0], swap[1])

