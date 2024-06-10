
n = int(input())
nums = list(map(int, input().split()))
from collections import Counter

freq = Counter(nums)
count = 0
for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        sum = nums[i] + nums[j]
        count += freq[sum]
print(count)

