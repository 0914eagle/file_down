
input()
nums = [int(x) for x in input().split()]

sorted_nums = sorted(nums)

diff = [abs(a - b) for a, b in zip(nums, sorted_nums)]

print(sum(diff))

