
from collections import defaultdict

n = int(input())
dict = defaultdict(list)

for i in range(n):
    s = input()
    dict[len(s)].append(s)

keys = list(dict.keys())
keys.sort()

res = 0

for key in keys:
    for s in dict[key]:
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if (s[:j] in dict[j]) and (s[-i:] in dict[i]):
                    res = max(res, i + j)

print(res)

