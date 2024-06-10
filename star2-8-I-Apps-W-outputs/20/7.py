
from itertools import combinations


def prod_modulo(nums, modulo):
    result = 1
    for num in nums:
        result = (result * num) % modulo
    return result


def solve(nums, modulo):
    diffs = [abs(a - b) for a, b in combinations(nums, 2)]
    return prod_modulo(diffs, modulo)


n, m = map(int, input().split())
nums = list(map(int, input().split()))
result = solve(nums, m)
print(result)

