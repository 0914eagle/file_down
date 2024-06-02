
def find_candidates(n, m, relations, wishes):
    graph = {i: [] for i in range(1, n+1)}
    for p, q in relations:
        graph[q].append(p)

    ancestors = set()
    candidates = []
    for i in range(n, 0, -1):
        if all(ancestor in ancestors for ancestor in graph[i]):
            candidates.append(i)
            ancestors.add(i)

    if len(candidates) == n:
        print(len(candidates))
        for c in reversed(candidates):
            print(c)
    else:
        print(-1)

# Input parsing
n, m = map(int, input().split())
relations = [tuple(map(int, input().split())) for _ in range(m)]
wishes = list(map(int, input().split()))

find_candidates(n, m, relations, wishes)
