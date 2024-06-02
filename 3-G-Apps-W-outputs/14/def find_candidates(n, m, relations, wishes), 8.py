
def find_candidates(n, m, relations, wishes):
    graph = {i: [] for i in range(1, n + 1)}
    for p, q in relations:
        graph[q].append(p)

    ancestors = set()
    for i in range(1, n + 1):
        ancestors.add(i)
        stack = [i]
        while stack:
            current = stack.pop()
            for parent in graph[current]:
                ancestors.add(parent)
                stack.append(parent)

    candidates = []
    for i in range(n, 0, -1):
        if wishes[i - 1] not in ancestors:
            return -1
        if wishes[i - 1] in candidates:
            candidates.remove(wishes[i - 1])
        candidates.insert(0, i)

    return candidates

# Input parsing
n, m = map(int, input().split())
relations = [list(map(int, input().split())) for _ in range(m)]
wishes = list(map(int, input().split()))

# Find candidates
result = find_candidates(n, m, relations, wishes)

# Output
if result == -1:
    print(-1)
else:
    print(len(result))
    for man in result:
        print(man)
