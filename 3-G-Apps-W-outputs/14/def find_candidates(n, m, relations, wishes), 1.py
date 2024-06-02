
def find_candidates(n, m, relations, wishes):
    graph = {i: [] for i in range(1, n + 1)}
    for p, q in relations:
        graph[q].append(p)

    ancestors = set()
    for i in range(1, n + 1):
        ancestors.add(i)
        queue = [i]
        while queue:
            current = queue.pop()
            for parent in graph[current]:
                if parent not in ancestors:
                    ancestors.add(parent)
                    queue.append(parent)

    candidates = []
    for i in range(n, 0, -1):
        if wishes[i - 1] in ancestors:
            candidates.append(i)

    if len(candidates) == 0:
        print(-1)
    else:
        print(len(candidates))
        for candidate in reversed(candidates):
            print(candidate)

# Input parsing
n, m = map(int, input().split())
relations = [list(map(int, input().split())) for _ in range(m)]
wishes = list(map(int, input().split()))

find_candidates(n, m, relations, wishes)
