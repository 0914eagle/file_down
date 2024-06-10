
import sys
import heapq


def find_max_lemonade(n, offers):
    graph = {}
    for offer in offers:
        offered, wanted, rate = offer
        graph.setdefault(offered, []).append((wanted, rate))
    pq = [(0, "pink")]
    visited = set()
    max_lemonade = 0
    while pq:
        curr_lemonade, curr_child = heapq.heappop(pq)
        if curr_child in visited:
            continue
        visited.add(curr_child)
        if curr_child == "blue":
            max_lemonade = max(max_lemonade, -curr_lemonade)
            continue
        for next_child, rate in graph.get(curr_child, []):
            heapq.heappush(pq, (-curr_lemonade * rate, next_child))
    return min(max_lemonade, 10)


def main():
    n = int(sys.stdin.readline())
    offers = []
    for _ in range(n):
        offers.append(sys.stdin.readline().split())
    print(find_max_lemonade(n, offers))


if __name__ == "__main__":
    main()


