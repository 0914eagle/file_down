
from collections import defaultdict
from typing import List


def bfs(adj_list: List[List[int]], start: int) -> List[int]:
    distance = defaultdict(lambda: float("inf"))
    queue = [start]
    distance[start] = 0
    while queue:
        cur = queue.pop(0)
        for neigh in adj_list[cur]:
            if distance[neigh] == float("inf"):
                distance[neigh] = distance[cur] + 1
                queue.append(neigh)
    return distance


def get_min_distance(adj_list: List[List[int]]) -> List[List[int]]:
    min_distance = []
    for start in range(len(adj_list)):
        distance = bfs(adj_list, start)
        min_distance.append(distance)
    return min_distance


def main():
    n, m = map(int, input().split())
    adj_list = [[] for _ in range(n)]
    for _ in range(m):
        a, b, w = map(int, input().split())
        adj_list[a - 1].append(b - 1)
        adj_list[b - 1].append(a - 1)
    q = int(input())
    min_distance = get_min_distance(adj_list)
    for _ in range(q):
        s, t = map(int, input().split())
        print(min_distance[s - 1][t - 1])


if __name__ == "__main__":
    main()

