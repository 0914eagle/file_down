
#!/usr/bin/env python
from collections import defaultdict, deque
import bisect
import math


class Fenwick:
    def __init__(self, n, initial_arr=[]):
        self.n = n
        self.arr = [0 for _ in range(n)]
        for i in range(len(initial_arr)):
            self.update(i, initial_arr[i])

    def update(self, pos, val):
        while pos < self.n:
            self.arr[pos] += val
            pos |= pos + 1

    def sum(self, pos):
        res = 0
        while pos >= 0:
            res += self.arr[pos]
            pos = (pos & (pos + 1)) - 1
        return res

    def __str__(self):
        return str(self.arr)


def solve(queries, n):
    intervals = []
    low = Fenwick(n)
    high = Fenwick(n)

    def add(i, x, y):
        intervals.append((x, y))
        low.update(i, x)
        high.update(i, y)

    def find_high(pos, val):
        res = 0
        while pos < high.n:
            res += high.arr[pos]
            pos |= pos + 1
        return bisect.bisect_left(res, val)

    def find_low(pos, val):
        res = 0
        while pos >= 0:
            res += low.arr[pos]
            pos = (pos & (pos + 1)) - 1
        return bisect.bisect_left(res, val)

    for q, x, y in queries:
        if q == 1:
            add(len(intervals), x, y)
        else:
            x, y = intervals[x - 1]
            if (x < intervals[y - 1][0] and y > intervals[y - 1][1]):
                print("YES")
            else:
                print("NO")


def main():
    n = int(input())
    queries = []
    for _ in range(n):
        q, x, y = input().split()
        queries.append((int(q), int(x), int(y)))
    solve(queries, n)


main()
