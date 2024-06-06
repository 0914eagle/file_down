
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    IOUs = defaultdict(int)

    for _ in range(m):
        a, b, c = map(int, input().split())
        IOUs[(a, b)] += c

    def find_cycle(visited, n, m, a, b, c, start):
        if (n, m) == (a, b):
            return True
        if (n, m) in visited:
            return False
        visited.add((n, m))
        return find_cycle(visited, m, IOUs[(m, n)], a, b, c, start)

    cycles = []
    for (a, b), c in IOUs.items():
        if (a, b) in cycles:
            continue
        if c == 0:
            continue
        visited = set()
        if find_cycle(visited, a, b, a, b, c, (a, b)):
            cycles.append((a, b))

    for (a, b), c in IOUs.items():
        if (a, b) in cycles:
            IOUs[(b, a)] = min(IOUs[(b, a)], IOUs[(a, b)])

    IOUs = dict(IOUs)
    for (a, b), c in IOUs.items():
        if c == 0:
            del IOUs[(a, b)]

    print(len(IOUs))
    for (a, b), c in IOUs.items():
        print(a, b, c)

solve()
