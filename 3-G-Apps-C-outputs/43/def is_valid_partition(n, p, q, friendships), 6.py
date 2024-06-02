
def is_valid_partition(n, p, q, friendships):
    adj_list = [[] for _ in range(n)]
    for i, friends in enumerate(friendships):
        for friend in friends:
            adj_list[i].append(friend)
            adj_list[friend].append(i)

    visited = [False] * n
    group = [-1] * n
    group_count = 0

    def dfs(node, current_group):
        if visited[node]:
            return
        visited[node] = True
        group[node] = current_group
        for neighbor in adj_list[node]:
            if group[neighbor] == current_group:
                return False
            if group[neighbor] == -1 and not dfs(neighbor, 1 - current_group):
                return False
        return True

    for i in range(n):
        if not visited[i]:
            if group_count >= p:
                return "detention"
            if not dfs(i, 0):
                return "detention"
            group_count += 1

    if group_count <= p and all(len(set(group[i] for i in group_members)) <= q for group_members in group):
        return "home\n" + str(group_count) + "\n" + "\n".join(" ".join(str(i) for i in group_members) for group_members in group)
    else:
        return "detention"

# Input parsing
n, p, q = map(int, input().split())
friendships = []
for _ in range(n):
    m, *friends = map(int, input().split())
    friendships.append(friends)

# Call the function and print the result
print(is_valid_partition(n, p, q, friendships))
