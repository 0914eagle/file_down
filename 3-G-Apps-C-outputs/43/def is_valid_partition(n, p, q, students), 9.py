
def is_valid_partition(n, p, q, students):
    graph = {i: set(friends) for i, *friends in students}
    visited = [False] * n
    groups = []

    def dfs(node, group):
        if len(group) > p:
            return False
        visited[node] = True
        group.append(node)
        for friend in graph[node]:
            if visited[friend] or len(group) + len(graph[friend]) > p + q:
                continue
            if not dfs(friend, group):
                return False
        return True

    for i in range(n):
        if not visited[i]:
            group = []
            if not dfs(i, group):
                return "detention"
            groups.append(group)

    return "home\n" + str(len(groups)) + "\n" + "\n".join([str(len(group)) + " " + " ".join(map(str, group)) for group in groups])

# Input parsing
n, p, q = map(int, input().split())
students = [list(map(int, input().split()))[1:] for _ in range(n)]

# Output
print(is_valid_partition(n, p, q, students))
