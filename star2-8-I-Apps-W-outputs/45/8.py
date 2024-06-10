
from collections import defaultdict


def solve(n, m, roads):
    degrees_in = defaultdict(int)
    degrees_out = defaultdict(int)
    for start, end in roads:
        degrees_out[start] += 1
        degrees_in[end] += 1
    max_equal = 0
    for start, end in roads:
        if degrees_in[start] == degrees_out[start]:
            max_equal += 1
    return max_equal


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        roads = []
        for _ in range(m):
            start, end = map(int, input().split())
            roads.append((start, end))
        max_equal = solve(n, m, roads)
        print(max_equal)

