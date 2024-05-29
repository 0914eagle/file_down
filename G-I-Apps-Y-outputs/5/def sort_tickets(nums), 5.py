
def sort_tickets(nums):
    return sorted(nums)

input_nums = list(map(int, input().split()))
result = sort_tickets(input_nums[1:])
print(*result)
```
