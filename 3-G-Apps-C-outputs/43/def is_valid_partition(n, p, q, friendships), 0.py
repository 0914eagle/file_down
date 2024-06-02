
def is_valid_partition(n, p, q, friendships):
    graph = {i: set(friends) for i, *friends in friendships}
    
    def dfs(node, group):
        if node in visited:
            return
        visited.add(node)
        groups[group].append(node)
        for friend in graph[node]:
            if friend not in visited:
                dfs(friend, group)
    
    visited = set()
    groups = []
    
    for i in range(n):
        if i not in visited:
            groups.append([])
            dfs(i, len(groups) - 1)
    
    for group in groups:
        internal_friends = 0
        external_friends = 0
        for student in group:
            internal_friends += sum(1 for friend in graph[student] if friend in group)
            external_friends += sum(1 for friend in graph[student] if friend not in group)
            if internal_friends > p or external_friends > q:
                return "detention"
    
    return "home\n" + str(len(groups)) + "\n" + "\n".join([str(len(group)) + " " + " ".join(map(str, group)) for group in groups])

# Input parsing
n, p, q = map(int, input().split())
friendships = [list(map(int, input().split())) for _ in range(n)]

# Output
print(is_valid_partition(n, p, q, friendships))
