
from heapq import heappush, heappop
from itertools import chain
from collections import defaultdict


def read_input():
    q = int(input())
    queries = [input().split() for _ in range(q)]
    return q, queries


def solve(q, queries):
    left = defaultdict(int)
    right = defaultdict(int)
    for op, *args in queries:
        if op == "1":
            a, b = map(int, args)
            left[a] += 1
            right[a + 1] -= 1
        elif op == "2":
            minimum = -1e18
            minimum_x = -1
            for x, (l, r) in enumerate(chain(left.items(), right.items())):
                if l != 0:
                    minimum_x = x
                if r != 0:
                    minimum = min(minimum, x + abs(x - minimum_x) + r)
            print(minimum_x, minimum)


def main():
    q, queries = read_input()
    solve(q, queries)


if __name__ == "__main__":
    main()

