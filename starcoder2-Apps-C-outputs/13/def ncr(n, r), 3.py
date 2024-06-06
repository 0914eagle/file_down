
# 思路：
# 1. 统计每个字符出现的次数
# 2. 统计每个字符出现的次数的组合数
# 3. 统计组合数的最大值

from collections import Counter
from itertools import combinations
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(lambda x, y: x*y, range(n, n-r, -1), 1)
    denom = reduce(lambda x, y: x*y, range(1, r+1), 1)
    return numer / denom

s = input()

c = Counter(s)

res = 0
for i in range(1, len(s)+1):
    for j in combinations(c.values(), i):
        res += reduce(lambda x, y: x*y, j)

print(res)
