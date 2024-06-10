
from itertools import accumulate

n = int(input())
nums = list(map(int, input().split()))

sums = list(accumulate(nums))
prods = list(accumulate(nums, lambda x, y: x * y))

counts = {}
for i in range(n):
    for j in range(i + 1, n + 1):
        diff = sums[j - 1] - sums[i - 1]
        prod = prods[j - 1] // prods[i - 1]
        if diff == prod:
            counts[(diff, prod)] = counts.get((diff, prod), 0) + 1

print(sum(counts.values()))

