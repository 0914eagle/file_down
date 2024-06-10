
from collections import defaultdict

n = int(input())
nums = list(map(int, input().split()))

prefix_sum = defaultdict(list)
curr_sum = 0
for i, num in enumerate(nums):
    curr_sum += num
    prefix_sum[curr_sum].append(i)

total = 0
for i, num in enumerate(nums):
    curr_sum = 0
    for j in range(i, len(nums)):
        curr_sum += nums[j]
        if curr_sum in prefix_sum and i in prefix_sum[curr_sum]:
            total += prefix_sum[curr_sum].count(i) - 1
print(total)

