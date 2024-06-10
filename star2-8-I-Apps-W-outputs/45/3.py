
from collections import defaultdict
from collections import Counter
from typing import List
import sys


def solve(n: int, m: int, roads: List[List[int]]) -> int:
    
    graph = defaultdict(set)
    for u, v in roads:
        graph[u].add(v)

    city_counts = Counter()
    for city in graph:
        city_counts[len(graph[city])] += 1
    for city in graph:
        city_counts[len(graph[city])] -= 1
        city_counts[len(graph[city]) - 1] += 1
    max_count = 0
    max_city = None
    for city, count in city_counts.items():
        if count > max_count:
            max_count = count
            max_city = city

    return max_city


def main():
    testcases = int(input())
    for _ in range(testcases):
        n, m = map(int, input().split())
        roads = []
        for _ in range(m):
            u, v = map(int, input().split())
            roads.append([u, v])
        print(solve(n, m, roads))


if __name__ == "__main__":
    main()


