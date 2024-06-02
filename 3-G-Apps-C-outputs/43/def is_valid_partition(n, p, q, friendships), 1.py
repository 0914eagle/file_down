
def is_valid_partition(n, p, q, friendships):
    adj_list = [[] for _ in range(n)]
    for i, friends in enumerate(friendships):
        for friend in friends[1:]:
            adj_list[i].append(friend)
            adj_list[friend].append(i)

    visited = [False] * n
    groups = []

    def dfs(node, group):
        visited[node] = True
        group.append(node)
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                dfs(neighbor, group)

    for i in range(n):
        if not visited[i]:
            group = []
            dfs(i, group)
            groups.append(group)

    for group in groups:
        inside_edges = 0
        for student in group:
            for friend in adj_list[student]:
                if friend not in group:
                    inside_edges += 1
        if len(group) > p or inside_edges > q:
            return "detention"

    return "home\n" + str(len(groups)) + "\n" + "\n".join([str(len(group)) + " " + " ".join(map(str, group)) for group in groups])

# Input parsing
n, p, q = map(int, input().split())
friendships = []
for _ in range(n):
    m, *friends = map(int, input().split())
    friendships.append((m, friends))

# Call the function and print the result
print(is_valid_partition(n, p, q, friendships))
