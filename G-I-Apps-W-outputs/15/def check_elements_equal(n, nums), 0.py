
def check_elements_equal(n, nums):
    if n == 1:
        return "YES"
    
    nums.sort()
    diff = nums[-1] - nums[0]
    
    for i in range(1, n - 1):
        if (nums[i] - nums[0]) % diff != 0:
            return "NO"
    
    return "YES"

# Input
n = int(input())
nums = list(map(int, input().split()))

# Output
print(check_elements_equal(n, nums))
```
