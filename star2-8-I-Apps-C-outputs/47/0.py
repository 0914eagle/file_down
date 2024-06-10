
from sys import stdin
n, m = map(int, input().split())
plants = [tuple(map(int, line.split())) for line in stdin]
num_replanted = 0
for i, plant in enumerate(plants):
    if plant[0] != i + 1:
        num_replanted += 1
print(num_replanted)

