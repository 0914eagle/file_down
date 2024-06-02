
def find_candidates(n, m, relations, wishes):
    graph = {i: [] for i in range(1, n + 1)}
    for p, q in relations:
        graph[q].append(p)

    ancestors = set()
    for i in range(1, n + 1):
        ancestors.add(i)
        for j in graph[i]:
            ancestors.add(j)

    candidates = []
    for i in range(n, 0, -1):
        if i in ancestors and i in wishes:
            candidates.append(i)

    if len(candidates) == 0:
        print(-1)
    else:
        print(len(candidates))
        for c in candidates:
            print(c)

# Input parsing
n, m = map(int, input().split())
relations = [list(map(int, input().split())) for _ in range(m)]
wishes = list(map(int, input().split()))

find_candidates(n, m, relations, wishes)
