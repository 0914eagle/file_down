
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
            if group[neighbor] == -1:
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
                q -= 1

    if q >= 0:
        print("home")
        print(group_count)
        for i in range(group_count):
            print(group_sizes[i], end=' ')
            for j in range(n):
                if group[j] == i:
                    print(j, end=' ')
            print()
    else:
        print("detention")

# Input parsing
n, p, q = map(int, input().split())
friendships = []
for _ in range(n):
    m, *friends = map(int, input().split())
    friendships.append(friends)

# Call the function with the input data
is_valid_partition(n, p, q, friendships)
