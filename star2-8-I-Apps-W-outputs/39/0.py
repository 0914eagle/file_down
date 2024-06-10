
from itertools import groupby
from operator import itemgetter


def solve(n, s, floors):
    
    # Sort passengers by arrival time
    floors = sorted(floors, key=itemgetter(1))
    # Group passengers by arrival time
    groups = groupby(floors, key=itemgetter(1))

    time = 0
    for _, group in groups:
        group = list(group)
        time += len(group) + 1  # Add 1 second for each group
        time += s - max(floor for floor, _ in group)  # Add the time to go to the highest floor in the group
    return time


if __name__ == '__main__':
    n, s = map(int, input().split())
    floors = [tuple(map(int, input().split())) for _ in range(n)]
    print(solve(n, s, floors))


