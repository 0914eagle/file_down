
def max_operations(n, m, nums, pairs):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    def can_divide(pair, v):
        i, j = pair
        return nums[i-1] % v == 0 and nums[j-1] % v == 0
    
    def divide_pair(pair, v):
        i, j = pair
        nums[i-1] //= v
        nums[j-1] //= v
    
    max_ops = 0
    for pair in pairs:
        i, j = pair
        v = gcd(nums[i-1], nums[j-1])
        while v > 1 and can_divide(pair, v):
            divide_pair(pair, v)
            max_ops += 1
            v = gcd(nums[i-1], nums[j-1])
    
    return max_ops

# Input
n, m = map(int, input().split())
nums = list(map(int, input().split()))
pairs = [list(map(int, input().split())) for _ in range(m)]

# Output
print(max_operations(n, m, nums, pairs))
