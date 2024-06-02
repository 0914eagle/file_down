
def find_candidates(n, m, relations, wishes):
    graph = {i: [] for i in range(1, n+1)}
    for p, q in relations:
        graph[q].append(p)
    
    ancestors = {i: set() for i in range(1, n+1)}
    for i in range(1, n+1):
        stack = [i]
        while stack:
            curr = stack.pop()
            for ancestor in graph[curr]:
                ancestors[i].add(ancestor)
                stack.append(ancestor)
    
    candidates = []
    for i in range(1, n+1):
        if all(wish in ancestors[i] for wish in wishes):
            candidates.append(i)
    
    if not candidates:
        print(-1)
    else:
        print(len(candidates))
        for candidate in candidates:
            print(candidate)

# Input parsing
n, m = map(int, input().split())
relations = [list(map(int, input().split())) for _ in range(m)]
wishes = list(map(int, input().split()))

find_candidates(n, m, relations, wishes)
