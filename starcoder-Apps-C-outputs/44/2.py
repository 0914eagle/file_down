
# USACO 2017 December Contest, Gold
# Problem 1. Aroma's Search
# https://usaco.guide/solutions/usaco-2017-dec-gold-p1

from typing import List


def read_ints() -> List[int]:
    return list(map(int, input().split()))


def main():
    x0, y0, ax, ay, bx, by = read_ints()
    xs, ys, t = read_ints()

    best = 0
    x, y = x0, y0
    dist = abs(x - xs) + abs(y - ys)
    while dist <= t:
        best += 1
        t -= dist
        x, y = ax * x + bx, ay * y + by
        dist = abs(x - xs) + abs(y - ys)

    print(best)


if __name__ == "__main__":
    main()
