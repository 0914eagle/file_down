
n = int(input())
nums = list(map(int, input().split()))

left, right = 0, 1
sum_val, prod_val = nums[left], nums[right]
num_ways = 0
while right < n:
    if sum_val == prod_val:
        num_ways += 1
    if right - left == 1:
        right += 1
        sum_val += nums[right]
        prod_val *= nums[right]
    else:
        sum_val -= nums[left]
        prod_val //= nums[left]
        left += 1
print(num_ways)

