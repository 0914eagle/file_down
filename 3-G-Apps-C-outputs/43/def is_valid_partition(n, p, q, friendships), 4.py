
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
        if len(group) < 1 or len(group) > p:
            return "detention"
        
        outside_friends = set()
        for student in group:
            outside_friends.update(graph[student] - set(group))
        
        if len(outside_friends) > q:
            return "detention"
    
    return "home", len(groups), *[" ".join(map(str, [len(group)] + group)) for group in groups]

# Input parsing
n, p, q = map(int, input().split())
friendships = [list(map(int, input().split()))[1:] for _ in range(n)]

# Output
result = is_valid_partition(n, p, q, friendships)
for line in result:
    print(line)
