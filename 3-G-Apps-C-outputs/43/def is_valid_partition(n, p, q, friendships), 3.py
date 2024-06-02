
def is_valid_partition(n, p, q, friendships):
    adj_list = {i: set(friends) for i, friends in enumerate(friendships)}

    def dfs(node, group):
        if node in visited:
            return
        visited.add(node)
        groups[group].append(node)
        for friend in adj_list[node]:
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
        external_friends = set()
        for student in group:
            for friend in adj_list[student]:
                if friend in group:
                    internal_friends += 1
                else:
                    external_friends.add(friend)
        if internal_friends > p * len(group) or len(external_friends) > q:
            return "detention"

    return "home", len(groups), groups

# Input parsing
n, p, q = map(int, input().split())
friendships = []
for _ in range(n):
    m, *friends = map(int, input().split())
    friendships.append(friends)

# Call the function and print the output
result = is_valid_partition(n, p, q, friendships)
if result == "home":
    print("home")
    print(result[1])
    for group in result[2]:
        print(len(group), *group)
else:
    print("detention")
