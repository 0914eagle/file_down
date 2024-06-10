
from itertools import permutations
import sys

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def solve(n, m, shops):
    min_distance = float("inf")
    for order in permutations(range(n)):
        dist = 0
        pos = (0, 0)
        for i in order:
            dist += distance(pos, shops[i])
            pos = shops[i]
        dist += distance(pos, (0, 0))
        min_distance = min(min_distance, dist)

    return min_distance


def main():
    n, m = map(int, input().split())
    shops = []
    for _ in range(n):
        x, y, t = map(int, input().split())
        shops.append((x, y, t))
    result = solve(n, m, shops)
    print(result)


if __name__ == "__main__":
    main()


