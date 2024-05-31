
from collections import Counter

def count_ways_to_choose_people(n, names):
    count = Counter([name[0] for name in names])
    ways = 0
    for c in "MARCH":
        ways += count[c] * (count["A"] - (c == "A")) * (count["R"] - (c == "R")) * (count["C"] - (c == "C")) * (count["H"] - (c == "H"))
    return ways // 6

# Input
n = int(input())
names = [input().strip() for _ in range(n)]

# Output
print(count_ways_to_choose_people(n, names))
