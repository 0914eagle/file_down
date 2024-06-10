
from collections import deque


def solve(n, fired, hired):
    firing_queue = deque()
    fired_count = 0
    hired_count = 0
    for i in range(n):
        fired_count += fired[i]
        hired_count += hired[i]
        while fired_count > 0:
            firing_queue.append(hired_count)
            fired_count -= 1
        while len(firing_queue) > 0 and firing_queue[0] == hired_count:
            firing_queue.popleft()
        print(hired_count, end=" ")


n = int(input())
fired = [int(x) for x in input().split()]
hired = [int(x) for x in input().split()]
solve(n, fired, hired)

