
from typing import List
import sys

input = sys.stdin.readline


def find_closest(num_of_citizens: int, d: int, pos: List[List[int]]) -> int:
    pos.sort(key=lambda x: (x[0], x[1]))
    min_dist = sys.maxsize

    for i in range(num_of_citizens - 1):
        dist_between_points = pos[i + 1][0] - pos[i][0]
        if dist_between_points > d:
            break

        diff = d - dist_between_points

        for j in range(i, num_of_citizens):
            if abs(pos[i][1] - pos[j][1]) <= diff:
                min_dist = min(min_dist, dist_between_points + abs(pos[i][1] - pos[j][1]))

    return min_dist if min_dist != sys.maxsize else "impossible"


num_of_citizens = int(input())
pos = []

for _ in range(num_of_citizens):
    pos.append(list(map(int, input().rstrip().split())))

d = int(input())

print(find_closest(num_of_citizens, d, pos))
