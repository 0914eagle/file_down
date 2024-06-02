
def is_valid_partition(n, p, q, friendships):
    groups = []
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            group = set()
            stack = [i]
            while stack:
                current = stack.pop()
                if current in group:
                    continue
                group.add(current)
                visited[current] = True
                for friend in friendships[current]:
                    if friend not in group:
                        stack.append(friend)
            groups.append(group)

    for group in groups:
        internal_friends = 0
        external_friends = set()
        for student in group:
            for friend in friendships[student]:
                if friend in group:
                    internal_friends += 1
                else:
                    external_friends.add(friend)
        if internal_friends > p or len(external_friends) > q:
            return "detention"
    
    return "home\n" + str(len(groups)) + "\n" + "\n".join([str(len(group)) + " " + " ".join(map(str, group)) for group in groups])

# Input parsing
n, p, q = map(int, input().split())
friendships = []
for _ in range(n):
    m, *friends = map(int, input().split())
    friendships.append(friends)

# Check validity of partition
result = is_valid_partition(n, p, q, friendships)
print(result)
