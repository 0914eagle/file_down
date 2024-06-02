
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
        visited[node] = True
        group[node] = current_group
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                dfs(neighbor, current_group)

    for i in range(n):
        if not visited[i]:
            dfs(i, group_count)
            group_count += 1

    group_sizes = [0] * group_count
    for g in group:
        group_sizes[g] += 1

    for i, friends in enumerate(friendships):
        for friend in friends:
            if group[i] == group[friend]:
                group_sizes[group[i]] -= 1

    for size in group_sizes:
        if size < 1 or size > p:
            return "detention"

    valid_partition = []
    for i in range(group_count):
        valid_partition.append([j for j, g in enumerate(group) if g == i])

    return "home", group_count, valid_partition

# Input parsing
n, p, q = map(int, input().split())
friendships = []
for _ in range(n):
    m, *friends = map(int, input().split())
    friendships.append(friends)

# Check if valid partition exists
result = is_valid_partition(n, p, q, friendships)

# Output
if result == "detention":
    print("detention")
else:
    print("home")
    print(result[1])
    for group in result[2]:
        print(len(group), *group)
