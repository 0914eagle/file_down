
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_common_factors(nums):
    common_factors = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            common = gcd(nums[i], nums[j])
            if common != 1:
                common_factors.add(common)
    return common_factors

def count_arrangements(n, nums):
    common_factors = find_common_factors(nums)
    num_arrangements = len(common_factors) if len(common_factors) > 0 else 1
    return num_arrangements % (10**9 + 7)

# Input reading
n = int(input())
nums = [int(input()) for _ in range(n)]

# Calculate and output the result
result = count_arrangements(n, nums)
print(result)
