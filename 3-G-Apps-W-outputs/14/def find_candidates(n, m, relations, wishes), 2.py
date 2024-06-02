
def find_candidates(n, m, relations, wishes):
    graph = {i: [] for i in range(1, n + 1)}
    for p, q in relations:
        graph[q].append(p)

    ancestors = [0] * (n + 1)
    for i in range(1, n + 1):
        ancestors[i] = i
        for parent in graph[i]:
            ancestors[i] = max(ancestors[i], ancestors[parent])

    candidates = []
    for i in range(1, n + 1):
        if ancestors[i] not in wishes:
            return -1
        candidates.append(i)

    return candidates

# Input parsing
n, m = map(int, input().split())
relations = [list(map(int, input().split())) for _ in range(m)]
wishes = list(map(int, input().split()))

result = find_candidates(n, m, relations, wishes)
if result == -1:
    print(-1)
else:
    print(len(result))
    for man in result:
        print(man)
