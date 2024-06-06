
from itertools import combinations

n, t, c = map(int, input().split())
lst = list(map(int, input().split()))

count = 0

for i in range(n - c + 1):
    # 任意選c個
    # 這裡用了combination
    for temp in combinations(lst, c):
        # 判斷是否都小於t
        if all(i <= t for i in temp):
            count += 1

print(count)
