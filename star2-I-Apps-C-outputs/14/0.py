
def rhymes(a, b):
    min_len = min(len(a), len(b))
    for i in range(min_len, max(min_len - 3, 0), -1):
        if a[-i:] == b[-i:]:
            return True
    return False


def solve(statements):
    graph = {}
    for statement in statements:
        a, b = statement.split(" is ")
        if a not in graph:
            graph[a] = set()
        if b not in graph:
            graph[b] = set()
        graph[a].add(b)
        graph[b].add(a)
    for a, b in graph.items():
        for c in b:
            if rhymes(a, c):
                if c not in graph:
                    graph[c] = set()
                graph[a].add(c)
                graph[c].add(a)
    visited = set()
    for a in graph:
        if a in visited:
            continue
        queue = [a]
        while queue:
            curr = queue.pop(0)
            if curr in visited:
                continue
            visited.add(curr)
            for neighbor in graph[curr]:
                queue.append(neighbor)
    return len(visited) == len(graph)


n = int(input())
statements = [input() for _ in range(n)]
if solve(statements):
    print("yes")
else:
    print("wait what?")

