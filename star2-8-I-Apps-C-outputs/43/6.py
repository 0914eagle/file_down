
from itertools import groupby
n = int(input())
s = input()
groups = [len(list(group)) for key, group in groupby(s)]
res = 0
for i in range(len(groups)-1):
    res = max(res, groups[i]+groups[i+1]+1)
print(res)

