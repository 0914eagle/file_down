
import math

def is_pairwise_coprime(N, nums):
    for i in range(N):
        for j in range(i+1, N):
            if math.gcd(nums[i], nums[j]) != 1:
                return False
    return True

def is_setwise_coprime(N, nums):
    gcd_result = nums[0]
    for i in range(1, N):
        gcd_result = math.gcd(gcd_result, nums[i])
        if gcd_result == 1:
            return False
    return True

def determine_coprime_type(N, nums):
    if is_pairwise_coprime(N, nums):
        return "pairwise coprime"
    elif is_setwise_coprime(N, nums):
        return "setwise coprime"
    else:
        return "not coprime"

# Input parsing
N = int(input())
nums = list(map(int, input().split()))

# Determine coprime type
result = determine_coprime_type(N, nums)
print(result)
```
