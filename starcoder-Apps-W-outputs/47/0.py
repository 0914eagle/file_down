
# 莫名其妙的递归错误，没有找到
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return max(sum(nums[i] for i in range(len(nums) // 2)), sum(nums[i] for i in range(len(nums) // 2, len(nums))))
