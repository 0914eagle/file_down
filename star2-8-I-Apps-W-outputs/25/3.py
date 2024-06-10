
import sys
from itertools import groupby

n, m, k = map(int, input().split())
buildings = [int(input()) for _ in range(n)]
groups = [(k, len(list(v))) for k, v in groupby(buildings)]

total_noise = 0
total_empty = 0
for group in groups:
    group_building, group_size = group
    if total_empty >= k:
        total_noise += group_size
    else:
        total_noise += group_size * (group_building + 1)
        total_empty += (group_building - 1)

print(total_noise)


