
def find_candidates(n, m, relations, wishes):
    graph = {i: [] for i in range(1, n+1)}
    for p, q in relations:
        graph[q].append(p)

    ancestors = {}
    for i in range(1, n+1):
        ancestors[i] = {i}
        stack = [i]
        while stack:
            current = stack.pop()
            for ancestor in graph.get(current, []):
                ancestors[i].add(ancestor)
                stack.append(ancestor)

    candidates = []
    for i in range(1, n+1):
        if wishes[i-1] not in ancestors[i]:
            return -1

    for i in range(1, n+1):
        candidates.append((len(ancestors[i]), i))

    candidates.sort(reverse=True)
    return [c[1] for c in candidates]

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
