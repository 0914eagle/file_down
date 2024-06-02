
def is_valid_partition(n, p, q, friendships):
    graph = {i: set(friends) for i, *friends in friendships}
    
    def is_valid_group(group):
        count_inside = sum(1 for student in group if any(student in graph[friend] for friend in group))
        return count_inside <= q
    
    def dfs(node, group):
        visited.add(node)
        group.append(node)
        for friend in graph[node]:
            if friend not in visited:
                dfs(friend, group)
    
    visited = set()
    groups = []
    for i in range(n):
        if i not in visited:
            group = []
            dfs(i, group)
            if len(group) > p or not is_valid_group(group):
                return "detention"
            groups.append(group)
    
    return "home\n" + str(len(groups)) + "\n" + "\n".join([str(len(group)) + " " + " ".join(map(str, group)) for group in groups])

# Input parsing
n, p, q = map(int, input().split())
friendships = [list(map(int, input().split())) for _ in range(n)]

# Call the function and print the output
print(is_valid_partition(n, p, q, friendships))
